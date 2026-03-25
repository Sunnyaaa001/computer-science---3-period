package com.whs.apiplatform.ai.tools;

import com.whs.apiplatform.ai.mapper.AIChattingHistoryMapper;
import com.whs.apiplatform.ai.service.AIChattingHistoryServiceImpl;
import com.whs.apiplatform.ai.service.IAIAgentService;
import com.whs.apiplatform.ai.service.IntentClassifier;
import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import dev.langchain4j.data.segment.TextSegment;
import dev.langchain4j.model.ollama.OllamaChatModel;
import dev.langchain4j.model.ollama.OllamaEmbeddingModel;
import dev.langchain4j.model.ollama.OllamaStreamingChatModel;
import dev.langchain4j.rag.content.retriever.ContentRetriever;
import dev.langchain4j.rag.content.retriever.EmbeddingStoreContentRetriever;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.store.embedding.EmbeddingStore;
import dev.langchain4j.store.embedding.redis.RedisEmbeddingStore;
import lombok.RequiredArgsConstructor;
import org.springframework.boot.autoconfigure.data.redis.RedisProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@RequiredArgsConstructor
public class AIConfig {

    private final AIChattingHistoryMapper chattingHistoryMapper;
    private final SnowflakeIdUtil snowflakeIdUtil;
    private final AiConfigProperties properties;
    private final RedisProperties redisProperties;

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
    public OllamaEmbeddingModel embeddingModel() {
        var cfg = properties.getEmbeddingChatModel();
        return OllamaEmbeddingModel.builder()
                .baseUrl(cfg.getBaseUrl())
                .modelName(cfg.getModelName())
                .timeout(cfg.getTimeout())
                .logRequests(cfg.getLogRequests())
                .logResponses(cfg.getLogResponses())
                .build();
    }

    @Bean
    public EmbeddingStore<TextSegment> embeddingStore() {
        return RedisEmbeddingStore.builder()
                .host(redisProperties.getHost())
                .port(redisProperties.getPort())
                .password(redisProperties.getPassword())
                .indexName("api_platform_vector")
                .user("default")
                .dimension(768)
                .prefix("tool:mapping:")
                .build();
    }


    @Bean
    public IntentClassifier intentClassifier(OllamaChatModel ollamaChatModel) {
        return AiServices.builder(IntentClassifier.class).
                chatLanguageModel(ollamaChatModel)
                .build();
    }

    @Bean
    public ContentRetriever contentRetriever(EmbeddingStore<TextSegment> embeddingStore,OllamaEmbeddingModel embeddingModel) {
        return EmbeddingStoreContentRetriever.builder()
                .embeddingModel(embeddingModel)
                .embeddingStore(embeddingStore)
                .maxResults(3)
                .minScore(0.6)
                .build();
    }


    @Bean("TopicAgent")
    public IAIAgentService TopicGeneratingAI(OllamaChatModel ollamaChatModel) {
        return AiServices.builder(IAIAgentService.class)
                .chatLanguageModel(ollamaChatModel)
                .build();
    }

    @Bean("chatAgent")
    public IAIAgentService GeneralTopicAI(OllamaStreamingChatModel chatModel) {
        return AiServices.builder(IAIAgentService.class)
                .streamingChatLanguageModel(chatModel)
                .chatMemoryProvider(memoryId -> new AIChattingHistoryServiceImpl(memoryId.toString(), chattingHistoryMapper, snowflakeIdUtil))
                .build();
    }

    @Bean("toolAgent")
    public IAIAgentService ToolsAIAssistant(OllamaStreamingChatModel model, APITool apiTool,ContentRetriever contentRetriever) {
        return AiServices.builder(IAIAgentService.class)
                .streamingChatLanguageModel(model)
//                .contentRetriever(contentRetriever)
                .tools(apiTool)
                .chatMemoryProvider(memoryId -> new AIChattingHistoryServiceImpl(memoryId.toString(), chattingHistoryMapper, snowflakeIdUtil))
                .build();
    }
}
