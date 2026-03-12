package com.whs.apiplatform.api.response;

import lombok.Data;

import java.util.Date;

@Data
public class ApiPluginResponse {
    private Long id;
    private Long apiId;
    private Character isLimited;
    private Character ipControl;
    private Character isUserLimited;
    private Date createTime;
    private Date updateTime;
}
