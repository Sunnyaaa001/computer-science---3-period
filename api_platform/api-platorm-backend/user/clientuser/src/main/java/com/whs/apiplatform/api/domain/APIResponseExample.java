package com.whs.apiplatform.api.domain;

import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class APIResponseExample extends BaseModel {

    private Long apiId;
    private String jsonExamples;
}
