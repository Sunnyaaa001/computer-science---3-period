package com.whs.apiplatform.ai.controller;


import com.whs.apiplatform.ai.request.AIUserInputMessage;
import com.whs.apiplatform.ai.router.AIAgentRouter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/client/aiAgent")
public class AIAgentController {

    @Autowired
    private AIAgentRouter aiAgentRouter;

    @PostMapping("/chat")
    public String chat(@RequestBody AIUserInputMessage message){
        return aiAgentRouter.chat(message);
    }
}
