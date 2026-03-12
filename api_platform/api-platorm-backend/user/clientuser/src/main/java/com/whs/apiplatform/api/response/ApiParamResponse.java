package com.whs.apiplatform.api.response;

import lombok.Data;

import java.util.Date;

@Data
public class ApiParamResponse {

    private Long id;
    private Long apiId;
    private String paramterName;
    private Character type;
    private String dataType;
    private String isRequired;
    private Date createTime;
    private Date updateTime;
}
