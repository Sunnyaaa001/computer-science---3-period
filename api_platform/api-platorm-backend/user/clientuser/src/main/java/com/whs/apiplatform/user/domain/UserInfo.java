package com.whs.apiplatform.user.domain;

import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class UserInfo extends BaseModel {
    private String username;
    private String password;
    private String avatar;
    private Character status;
}
