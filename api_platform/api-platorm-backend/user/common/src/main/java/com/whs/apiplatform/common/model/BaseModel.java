package com.whs.apiplatform.common.model;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import lombok.Data;

import java.util.Date;
@Data
public abstract class BaseModel {
    @JsonSerialize
    private Long id;
    private Date createTime;
    private Date updateTime;
}
