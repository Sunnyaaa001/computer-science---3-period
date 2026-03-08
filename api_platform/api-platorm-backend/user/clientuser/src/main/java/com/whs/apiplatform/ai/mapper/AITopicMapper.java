package com.whs.apiplatform.ai.mapper;

import com.whs.apiplatform.ai.domain.AITopics;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface AITopicMapper {

    int insertTopics(AITopics topics);
}
