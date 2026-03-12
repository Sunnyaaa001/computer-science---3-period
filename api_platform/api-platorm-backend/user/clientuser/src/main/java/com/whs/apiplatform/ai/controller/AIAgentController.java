package com.whs.apiplatform.ai.controller;

import com.whs.apiplatform.ai.request.AIUserInputMessage;
import com.whs.apiplatform.ai.router.AIAgentRouter;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;
import reactor.core.publisher.Flux;

@RestController
@RequestMapping("/client/aiAgent")
@RequiredArgsConstructor
public class AIAgentController {

    private final AIAgentRouter aiAgentRouter;

//    @PostMapping("/chat")
//    public String chat(@RequestBody AIUserInputMessage message){
//        return aiAgentRouter.chat(message);
//    }

    @PostMapping(value = "/chat/streaming",produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> chatStreaming(@RequestBody AIUserInputMessage message){
        return aiAgentRouter.chatStreaming(message);
    }
}
