package com.whs.apiplatform.api.response;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;

import java.util.Date;
import java.util.List;

@Data
@JsonIgnoreProperties(value = {"handler", "hibernateLazyInitializer"})
public class ApiInfoResponse {

    private Long id;
    private String categoryId;
    private String apiName;
    private String apiHost;
    private Integer apiPort;
    private String apiMethod;
    private String apiPath;
    private String endpoint;
    private Character isHttps;
    private Character status;
    private Long creator;
    private Date createTime;
    private Date updateTime;

    @JsonInclude(JsonInclude.Include.NON_NULL)
    private List<ApiParamResponse> params;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private ApiPluginResponse plugins;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private List<ApiResponsePropertyResponse> properties;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private ApiResponseExamplesResponse examples;



}
