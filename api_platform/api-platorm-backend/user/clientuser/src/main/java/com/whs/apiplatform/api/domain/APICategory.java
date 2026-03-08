package com.whs.apiplatform.api.domain;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class APICategory extends BaseModel {

    @JsonSerialize(using = ToStringSerializer.class)
    private Long parentId;
    private String categoryName;
    private Integer sort;
    private String ancestors;
    @JsonSerialize(using = ToStringSerializer.class)
    private Long creatorId;

}
