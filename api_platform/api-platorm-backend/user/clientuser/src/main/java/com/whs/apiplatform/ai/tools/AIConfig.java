package com.whs.apiplatform.ai.tools;

import com.whs.apiplatform.ai.mapper.AIChattingHistoryMapper;
import com.whs.apiplatform.ai.service.AIChattingHistoryServiceImpl;
import com.whs.apiplatform.ai.service.IAIAgentService;
import com.whs.apiplatform.ai.service.IntentClassifier;
import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import dev.langchain4j.memory.chat.MessageWindowChatMemory;
import dev.langchain4j.model.ollama.OllamaChatModel;
import dev.langchain4j.model.ollama.OllamaStreamingChatModel;
import dev.langchain4j.service.AiServices;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@RequiredArgsConstructor
public class AIConfig {

    private final AIChattingHistoryMapper chattingHistoryMapper;
    private final SnowflakeIdUtil snowflakeIdUtil;
    private final AiConfigProperties properties;

    @Bean
    public OllamaChatModel ollamaChatModel() {
        var cfg = properties.getChatModel();
        return OllamaChatModel.builder()
                .baseUrl(cfg.getBaseUrl())
                .modelName(cfg.getModelName())
                .temperature(cfg.getTemperature().doubleValue())
                .timeout(cfg.getTimeout())
                .maxRetries(cfg.getMaxRetries())
                .logRequests(cfg.getLogRequests())
                .logResponses(cfg.getLogResponses())
                .build();
    }

    @Bean
    public OllamaStreamingChatModel ollamaStreamingChatModel() {
        var cfg = properties.getStreamingChatModel();
        return OllamaStreamingChatModel.builder()
                .baseUrl(cfg.getBaseUrl())
                .modelName(cfg.getModelName())
                .temperature(cfg.getTemperature().doubleValue())
                .timeout(cfg.getTimeout())
                .logRequests(cfg.getLogRequests())
                .logResponses(cfg.getLogResponses())
                .build();
    }


    @Bean
    public IntentClassifier intentClassifier(OllamaChatModel ollamaChatModel) {
        return AiServices.builder(IntentClassifier.class).
                chatModel(ollamaChatModel)
                .build();
    }

    @Bean("TopicAgent")
    public IAIAgentService TopicGeneratingAI(OllamaChatModel ollamaChatModel) {
        return AiServices.builder(IAIAgentService.class)
                .chatModel(ollamaChatModel)
                .chatMemoryProvider(memoryId -> MessageWindowChatMemory.withMaxMessages(5)).build();
    }

    @Bean("chatAgent")
    public IAIAgentService GeneralTopicAI(OllamaStreamingChatModel chatModel) {
        return AiServices.builder(IAIAgentService.class)
                .streamingChatModel(chatModel)
                .chatMemoryProvider(memoryId -> new AIChattingHistoryServiceImpl(memoryId.toString(), chattingHistoryMapper, snowflakeIdUtil))
                .build();
    }

    @Bean("toolAgent")
    public IAIAgentService ToolsAIAssistant(OllamaStreamingChatModel model, APITool apiTool) {
        return AiServices.builder(IAIAgentService.class)
                .streamingChatModel(model)
                .tools(apiTool)
                .chatMemoryProvider(memoryId -> new AIChattingHistoryServiceImpl(memoryId.toString(), chattingHistoryMapper, snowflakeIdUtil))
                .build();
    }
}
