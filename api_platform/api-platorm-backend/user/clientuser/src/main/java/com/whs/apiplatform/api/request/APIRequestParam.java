package com.whs.apiplatform.api.request;

import java.util.Map;

public record APIRequestParam(
        Long apiId,
        Map<String,Object> params,
        Map<String,Object> headers
) {
}
