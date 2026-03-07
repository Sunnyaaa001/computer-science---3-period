package com.whs.apiplatform.user.request;

import jakarta.validation.constraints.NotBlank;
import lombok.Data;

public record LoginUser(
        @NotBlank(message = "username is empty")
        String username,
        @NotBlank(message = "password is empty")
        String password
) {
}
