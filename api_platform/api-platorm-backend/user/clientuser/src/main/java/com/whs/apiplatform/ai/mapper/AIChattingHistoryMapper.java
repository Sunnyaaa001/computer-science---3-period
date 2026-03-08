package com.whs.apiplatform.ai.mapper;

import com.whs.apiplatform.ai.domain.AIChattingHistory;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface AIChattingHistoryMapper {

    int insertHistory(AIChattingHistory AIChattingHistory);

    List<AIChattingHistory> selectHistoryList(Long topicId);

    int deleteHistoryByTopicId(Long topicId);
}
