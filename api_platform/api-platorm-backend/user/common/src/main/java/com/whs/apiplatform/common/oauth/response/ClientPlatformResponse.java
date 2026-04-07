package com.whs.apiplatform.common.oauth.response;

import lombok.Data;

@Data
public class ClientPlatformResponse {
    private String platformName;
    private String authorizeUrl;
}
