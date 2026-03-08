package com.whs.apiplatform.common.model;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import lombok.Data;

import java.util.Date;
@Data
public abstract class BaseModel {
    @JsonSerialize(using = ToStringSerializer.class)
    private Long id;
    private Date createTime;
    private Date updateTime;
}
