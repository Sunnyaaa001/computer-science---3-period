package com.whs.apiplatform.api.domain;

import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class APIParamInfo extends BaseModel {
    private Long apiId;
    private String paramterName;
    private Character type;
    private String dataType;
    private Character isRequired;
}