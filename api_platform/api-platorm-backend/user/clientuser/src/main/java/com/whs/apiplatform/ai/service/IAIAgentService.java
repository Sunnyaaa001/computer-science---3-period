package com.whs.apiplatform.ai.service;

import dev.langchain4j.service.MemoryId;
import dev.langchain4j.service.TokenStream;
import dev.langchain4j.service.UserMessage;
import reactor.core.publisher.Flux;

public interface IAIAgentService {
    String chat(@MemoryId String memoryId, @UserMessage String message);

    Flux<String> chatStream(@MemoryId String memoryId, @UserMessage String message);
}
