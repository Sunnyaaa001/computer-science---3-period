package com.whs.apiplatform.api.request;

import dev.langchain4j.agent.tool.P;

import java.util.Map;

public record APIAIRequestParam(
        @P("api name") String apiName,
        @P("headers") Map<String,Object> headers,
        @P("params") Map<String,Object> params
) {
}
