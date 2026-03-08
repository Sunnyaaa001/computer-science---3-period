package com.whs.apiplatform.ai.service;

import com.whs.apiplatform.ai.enums.AIRouterEnum;
import dev.langchain4j.service.SystemMessage;
import dev.langchain4j.service.UserMessage;

public interface IntentClassifier {

    @SystemMessage("""
        You are an intent classifier.

        Classify the user request.

        CHAT:
        - greetings (e.g., "Hi", "Hello")
        - normal conversation (e.g., "How are you?")
        - knowledge questions answered directly by AI 
          (e.g., "What is the capital of France?", "Can you give me the full name of China?")

        TOOL:
        - API platform or database queries 
          (e.g., "Get me the weather in Beijing via API", "Retrieve user info from the database")

        Rules:
        Return ONLY one of these values:
        CHAT,
        TOOL
        """)
    AIRouterEnum classify(@UserMessage String message);
}
