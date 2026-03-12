package com.whs.apiplatform.api.domain;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class APIPluginInfo extends BaseModel {

    @JsonSerialize(using = ToStringSerializer.class)
    private Long apiId;
}
