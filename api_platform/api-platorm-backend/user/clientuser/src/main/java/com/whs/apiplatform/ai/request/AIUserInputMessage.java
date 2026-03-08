package com.whs.apiplatform.ai.request;

import jakarta.validation.constraints.NotBlank;

public record AIUserInputMessage(
        Long topicId,
        @NotBlank(message = "message can't be blank!")
        String message
) {
}
