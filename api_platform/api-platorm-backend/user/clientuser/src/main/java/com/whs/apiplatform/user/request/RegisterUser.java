package com.whs.apiplatform.user.request;

import jakarta.validation.constraints.NotBlank;

public record RegisterUser(
        @NotBlank(message = "username is empty")
        String username,
        @NotBlank(message = "password is empty!")
        String password
) {
}
