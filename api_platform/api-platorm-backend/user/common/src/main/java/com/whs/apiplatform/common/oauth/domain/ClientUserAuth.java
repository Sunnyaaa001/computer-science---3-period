package com.whs.apiplatform.common.oauth.domain;

import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class ClientUserAuth extends BaseModel {
    private Long userId;
    private String platformType;
    private String subId;

}
