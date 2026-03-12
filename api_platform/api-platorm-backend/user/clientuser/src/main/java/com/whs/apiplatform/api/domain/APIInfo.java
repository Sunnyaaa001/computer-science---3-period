package com.whs.apiplatform.api.domain;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class APIInfo extends BaseModel {
    @JsonSerialize(using = ToStringSerializer.class)
    private Long categoryId;
    private String apiName;
    private Integer apiPort;
    private String apiMethod;
    private String apiPath;
    private String endPoint;
    private Character isHttps;
    private Character status;
    @JsonSerialize(using = ToStringSerializer.class)
    private Long creator;
}
