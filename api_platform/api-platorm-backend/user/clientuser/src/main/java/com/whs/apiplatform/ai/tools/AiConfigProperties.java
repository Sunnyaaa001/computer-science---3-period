package com.whs.apiplatform.ai.tools;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

import java.time.Duration;

@Data
@Configuration
@ConfigurationProperties(prefix = "langchain4j.ollama")
public class AiConfigProperties {
    private ChatModelConfig chatModel;
    private StreamingChatModelConfig streamingChatModel;
    private EmbeddingChatModelConfig embeddingChatModel;

    @Data
    public static class ChatModelConfig {
        private String baseUrl;
        private String modelName;
        private Double temperature;
        private Duration timeout;
        private Integer maxRetries;
        private Boolean logRequests;
        private Boolean logResponses;
    }

    @Data
    public static class StreamingChatModelConfig {
        private String baseUrl;
        private String modelName;
        private Double temperature;
        private Duration timeout;
        private Integer maxRetries;
        private Boolean logRequests;
        private Boolean logResponses;
    }

    @Data
    public static class EmbeddingChatModelConfig {
        private String baseUrl;
        private String modelName;
        private Double temperature;
        private Duration timeout;
        private Integer maxRetries;
        private Boolean logRequests;
        private Boolean logResponses;
    }
}
