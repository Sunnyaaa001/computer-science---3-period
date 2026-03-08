package com.whs.apiplatform.ai.service;

import com.whs.apiplatform.ai.domain.AIChattingHistory;
import com.whs.apiplatform.ai.mapper.AIChattingHistoryMapper;
import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import dev.langchain4j.data.message.AiMessage;
import dev.langchain4j.data.message.ChatMessage;
import dev.langchain4j.data.message.SystemMessage;
import dev.langchain4j.data.message.UserMessage;
import dev.langchain4j.memory.ChatMemory;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class AIChattingHistoryServiceImpl implements ChatMemory {


    private final String memoryId;
    private final AIChattingHistoryMapper chattingHistoryMapper;
    private final SnowflakeIdUtil snowflakeIdUtil;

    private final List<ChatMessage> transientMemory = new ArrayList<>();

    public AIChattingHistoryServiceImpl(String memoryId, AIChattingHistoryMapper chattingHistoryMapper, SnowflakeIdUtil snowflakeIdUtil) {
       this.memoryId = memoryId;
       this.chattingHistoryMapper = chattingHistoryMapper;
       this.snowflakeIdUtil = snowflakeIdUtil;
    }

    @Override
    public Object id() {
        return memoryId;
    }

    @Override
    @Transactional
    public void add(ChatMessage chatMessage) {
        transientMemory.add(chatMessage);
        String content = null;
        String type = null;
        if (chatMessage instanceof UserMessage){
            type = "USER";
            content =  ((UserMessage) chatMessage).singleText();
        }
        if (chatMessage instanceof SystemMessage){
            type = "SYSTEM";
            content = ((SystemMessage) chatMessage).text();
        }
        if (chatMessage instanceof AiMessage){
            AiMessage aiMessage = (AiMessage) chatMessage;
            content = aiMessage.text();
            if (content != null && !content.isEmpty()) {
                type = "AI";
                transientMemory.clear();
            } else {
                return;
            }
        }
        if (type != null && content != null && !content.trim().isEmpty()) {
            AIChattingHistory history = new AIChattingHistory();
            history.setId(snowflakeIdUtil.getId());
            history.setTopicId(Long.valueOf(memoryId.split(":")[1]));
            history.setType(type);
            history.setAiContent(content);
            history.setCreateTime(new Date());
            history.setUpdateTime(history.getCreateTime());

            chattingHistoryMapper.insertHistory(history);
        }

    }

    @Override
    public List<ChatMessage> messages() {
        Long topicId = Long.valueOf(memoryId.split(":")[1]);
        List<AIChattingHistory> historyList =  chattingHistoryMapper.selectHistoryList(topicId);
        List<ChatMessage> chatMessages = new ArrayList<>();
        for (AIChattingHistory history : historyList) {

            String type = history.getType();
            String content = history.getAiContent();
            if ("USER".equals(type)){
                chatMessages.add(UserMessage.from(content));
            }
            if ("SYSTEM".equals(type)){
                chatMessages.add(SystemMessage.from(content));
            }
            if ("AI".equals(type)){
                chatMessages.add(AiMessage.from(content));
            }
        }

        for (ChatMessage m : transientMemory) {
            if (!chatMessages.contains(m)) {
                chatMessages.add(m);
            }
        }
        return chatMessages;
    }

    @Override
    @Transactional
    public void clear() {
        Long topicId = Long.valueOf(memoryId.split(":")[1]);
        chattingHistoryMapper.deleteHistoryByTopicId(topicId);
    }
}
