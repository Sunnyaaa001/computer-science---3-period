package com.whs.apiplatform.ai.router;

import cn.hutool.core.util.ObjectUtil;
import com.whs.apiplatform.ai.domain.AITopics;
import com.whs.apiplatform.ai.enums.AIRouterEnum;
import com.whs.apiplatform.ai.mapper.AITopicMapper;
import com.whs.apiplatform.ai.request.AIUserInputMessage;
import com.whs.apiplatform.ai.service.IAIAgentService;
import com.whs.apiplatform.ai.service.IntentClassifier;
import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import com.whs.apiplatform.common.userinfo.UserInfoUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import java.util.Date;
import java.util.Map;
import java.util.concurrent.ExecutorService;

@Component
public class AIAgentRouter {

    private final IntentClassifier classifier;
    private final IAIAgentService chatAgent;
    private final IAIAgentService toolAgent;
    private final SnowflakeIdUtil idUtil;
    private final AITopicMapper topicMapper;
    private final IAIAgentService topicAgent;
    private final ExecutorService executorService;

    public AIAgentRouter(IntentClassifier classifier,
                    SnowflakeIdUtil idUtil,
                    AITopicMapper topicMapper,
                         ExecutorService executorService,
                    @Qualifier("chatAgent") IAIAgentService chatAgent,
                    @Qualifier("toolAgent") IAIAgentService toolAgent,
                         @Qualifier("TopicAgent") IAIAgentService topicAgent) {
        this.classifier = classifier;
        this.chatAgent = chatAgent;
        this.toolAgent = toolAgent;
        this.idUtil = idUtil;
        this.topicMapper = topicMapper;
        this.topicAgent = topicAgent;
        this.executorService = executorService;
    }

//    public String chat(AIUserInputMessage userInputMessage){
//        //get current userId
//        Map<String,Object> userInfo =  UserInfoUtil.getCurrentUserInfo();
//        Long userId = Long.parseLong(userInfo.get("id").toString());
//        String message = userInputMessage.message();
//        Long topicId = ensureTopicId(userInputMessage,userId);
//        String memoryId = userId+ ":" + topicId;
//        AIRouterEnum chatCategory  = classifier.classify(message);
//        if(chatCategory == AIRouterEnum.TOOL && looksLikeNormalQuestion(message)){
//            chatCategory = AIRouterEnum.CHAT;
//        }
//        String response =  switch (chatCategory){
//            case CHAT ->  chatAgent.chat(memoryId,message);
//            case TOOL -> toolAgent.chat(memoryId,message);
//            default -> "Sorry, I could not understand the request.";
//        };
//        return response;
//    }

    private boolean looksLikeNormalQuestion(String message){
        if(message == null) return false;
        String lower = message.toLowerCase();
        // TODO: from database
        return lower.matches(".*(capital|full name|population|currency|language|flag).*\\??");
    }

    public Long ensureTopicId(AIUserInputMessage userInputMessage,Long userId){
        Long topicId = userInputMessage.topicId();
        if(ObjectUtil.isNotEmpty(topicId)){
            return topicId;
        }
        // generate topic information
        topicId = idUtil.getId();
        AITopics topics = new AITopics();
        topics.setId(topicId);
        topics.setCreatorId(userId);
        topics.setCreateTime(new Date());
        topics.setUpdateTime(topics.getCreateTime());
        // let AI generate topic name
        String memoryId = userId + ":" + topicId;
        String message = "Generate a concise topic name (5–10 words) for this user message:" + userInputMessage.message() ;
        String topicName =  topicAgent.chat(memoryId,message);
        topics.setTopicName(topicName);
        topicMapper.insertTopics(topics);
        return topicId;
    }

    public SseEmitter chatStreaming(AIUserInputMessage userInputMessage) {
        // get current user
        Map<String,Object> userInfo =  UserInfoUtil.getCurrentUserInfo();
        Long userId = Long.parseLong(userInfo.get("id").toString());
        String message = userInputMessage.message();
        Long topicId = ensureTopicId(userInputMessage,userId);
        String memoryId = userId+ ":" + topicId;
        AIRouterEnum chatCategory  = classifier.classify(message);
        if(chatCategory == AIRouterEnum.TOOL && looksLikeNormalQuestion(message)){
            chatCategory = AIRouterEnum.CHAT;
        }
        SseEmitter emitter = new SseEmitter(60000L);
        AIRouterEnum finalChatCategory = chatCategory;
        executorService.submit(() -> {
            try {
                IAIAgentService selectedAgent = (finalChatCategory == AIRouterEnum.TOOL) ? toolAgent : chatAgent;

                selectedAgent.chatStream(memoryId, message)
                        .onNext(token -> {
                            try {
                                emitter.send(SseEmitter.event().data(token));
                            } catch (Exception e) {
                                emitter.completeWithError(e);
                            }
                        })
                        .onComplete(response -> emitter.complete())
                        .onError(emitter::completeWithError)
                        .start();
            } catch (Exception e) {
                emitter.completeWithError(e);
            }
        });
        return emitter;
    }
}
