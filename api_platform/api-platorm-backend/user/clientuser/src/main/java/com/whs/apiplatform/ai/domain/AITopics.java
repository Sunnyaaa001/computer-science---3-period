package com.whs.apiplatform.ai.domain;

import com.whs.apiplatform.common.model.BaseModel;
import lombok.Data;

@Data
public class AITopics extends BaseModel {

    private String topicName;
    private Long creatorId;
}