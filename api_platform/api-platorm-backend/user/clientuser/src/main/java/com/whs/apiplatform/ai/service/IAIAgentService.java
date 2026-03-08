package com.whs.apiplatform.ai.service;

import dev.langchain4j.service.MemoryId;
import dev.langchain4j.service.UserMessage;

public interface IAIAgentService {
    String chat(@MemoryId String memoryId, @UserMessage String message);
}
