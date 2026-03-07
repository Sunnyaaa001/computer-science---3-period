package com.whs.apiplatform.common.id;

import cn.hutool.core.lang.Snowflake;
import cn.hutool.core.util.IdUtil;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class SnowflakeIdUtil {
    @Value("${snowflake.workId:1}")
    private Long workId;
    @Value("${snowflake.instanceId:1}")
    private Long instanceId;

    private Snowflake snowflake;

    @PostConstruct
    private void init(){
        snowflake = IdUtil.getSnowflake(workId,instanceId);
    }

    public synchronized long getId() {
        return snowflake.nextId();
    }
}
