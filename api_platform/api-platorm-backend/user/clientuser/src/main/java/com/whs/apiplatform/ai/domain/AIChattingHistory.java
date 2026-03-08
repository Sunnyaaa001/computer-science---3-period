package com.whs.apiplatform.ai.domain;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class AIChattingHistory  extends BaseModel {

    @JsonSerialize(using = ToStringSerializer.class)
    private Long topicId;
    private String type;
    private String aiContent;
}
