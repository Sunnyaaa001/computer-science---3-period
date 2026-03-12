package com.whs.apiplatform.api.response;

import lombok.Data;

import java.util.Date;

@Data
public class ApiResponseExamplesResponse {
    private Long id;
    private Long apiId;
    private String jsonExamples;
    private Date createTime;
    private Date updateTime;
}
