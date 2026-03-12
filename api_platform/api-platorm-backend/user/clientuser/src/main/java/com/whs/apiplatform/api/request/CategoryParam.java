package com.whs.apiplatform.api.request;

import dev.langchain4j.agent.tool.P;

public record CategoryParam(
        @P("category name")
        String categoryName
) {
}
