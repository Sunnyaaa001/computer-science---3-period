package com.whs.apiplatform.common.oauth.domain;

import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class ClientPlatform extends BaseModel {
    private String platformName;
    private String clientId;
    private String clientSecret;
    private String authorizeUrl;
    private String usernameAttributeName;
    private String authorizedRedirectUrl;
    private String scope;
}
