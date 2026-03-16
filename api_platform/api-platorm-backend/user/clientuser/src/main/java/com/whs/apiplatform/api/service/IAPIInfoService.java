package com.whs.apiplatform.api.service;

import com.whs.apiplatform.api.request.APIRequestParam;
import com.whs.apiplatform.api.response.ApiInfoResponse;
import com.whs.apiplatform.api.response.ApiResponsePropertyResponse;
import com.whs.apiplatform.common.response.ResponseResult;

import java.util.List;
import java.util.Map;

public interface IAPIInfoService {

    ResponseResult<ApiInfoResponse> apiInfo(Long apiId);

    List<ApiInfoResponse> apiInfoList(Long categoryId);

    Map<String, Object> requestApi(APIRequestParam apiRequestParam);
}
