package com.whs.apiplatform.ai.tools;

import com.whs.apiplatform.ai.mapper.AIChattingHistoryMapper;
import com.whs.apiplatform.ai.service.AIChattingHistoryServiceImpl;
import com.whs.apiplatform.ai.service.IAIAgentService;
import com.whs.apiplatform.ai.service.IntentClassifier;
import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import dev.langchain4j.memory.chat.MessageWindowChatMemory;
import dev.langchain4j.model.ollama.OllamaChatModel;
import dev.langchain4j.service.AiServices;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AIConfig {

    private final AIChattingHistoryMapper chattingHistoryMapper;
    private final SnowflakeIdUtil snowflakeIdUtil;

    public AIConfig(AIChattingHistoryMapper chattingHistoryMapper,
                    SnowflakeIdUtil snowflakeIdUtil) {
        this.chattingHistoryMapper = chattingHistoryMapper;
        this.snowflakeIdUtil = snowflakeIdUtil;
    }

    @Bean
    public IntentClassifier intentClassifier(OllamaChatModel model) {
        return AiServices.builder(IntentClassifier.class)
                .chatLanguageModel(model)
                .build();
    }

    @Bean("TopicAgent")
    public IAIAgentService TopicGeneratingAI(OllamaChatModel model) {
        return AiServices.builder(IAIAgentService.class)
                .chatLanguageModel(model)
                .chatMemoryProvider(memoryId-> MessageWindowChatMemory.withMaxMessages(5)).build();
    }

    @Bean("chatAgent")
    public IAIAgentService GeneralTopicAI(OllamaChatModel model) {
        return AiServices.builder(IAIAgentService.class)
                .chatLanguageModel(model)
                .chatMemoryProvider(memoryId-> new AIChattingHistoryServiceImpl(memoryId.toString(),chattingHistoryMapper,snowflakeIdUtil))
                .build();
    }

    @Bean("toolAgent")
    public IAIAgentService ToolsAIAssistant(OllamaChatModel model,APITool apiTool) {
        return AiServices.builder(IAIAgentService.class)
                .chatLanguageModel(model)
                .tools(apiTool)
                .chatMemoryProvider(memoryId-> new AIChattingHistoryServiceImpl(memoryId.toString(),chattingHistoryMapper,snowflakeIdUtil))
                .build();
    }
}
