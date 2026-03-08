package com.whs.apiplatform.api.request;

import dev.langchain4j.model.output.structured.Description;

public record CategoryParam(
        @Description("API category name for API category name searching")
        String categoryName
) {
}
