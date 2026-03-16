package com.whs.apiplatform.api.service.impl;

import cn.hutool.core.util.StrUtil;
import cn.hutool.json.JSONUtil;
import com.whs.apiplatform.api.mapper.APIInfoMapper;
import com.whs.apiplatform.api.request.APIRequestParam;
import com.whs.apiplatform.api.response.ApiInfoResponse;
import com.whs.apiplatform.api.response.ApiResponsePropertyResponse;
import com.whs.apiplatform.api.service.IAPIInfoService;
import com.whs.apiplatform.common.http.HttpUtil;
import com.whs.apiplatform.common.response.ResponseResult;
import com.whs.apiplatform.common.tree.TreeUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class APIInfoServiceImpl implements IAPIInfoService {

    private final APIInfoMapper apiInfoMapper;

    private final HttpUtil httpUtil;

    @Override
    public ResponseResult<ApiInfoResponse> apiInfo(Long apiId) {
        ApiInfoResponse apiInfoResponse = apiInfoMapper.apiInfo(apiId);
        if (apiInfoResponse == null) {
            return ResponseResult.fail("API does not exist");
        }
        List<ApiResponsePropertyResponse> properties = TreeUtil.buildTree(apiInfoResponse.getProperties(), 0L);
        apiInfoResponse.setProperties(properties);
        return ResponseResult.success(apiInfoResponse);
    }

    @Override
    public List<ApiInfoResponse> apiInfoList(Long categoryId) {
        return apiInfoMapper.apiList(categoryId);
    }

    @Override
    public Map<String, Object> requestApi(APIRequestParam apiRequestParam) {
        // select API info in database
        ApiInfoResponse apiInfoResponse = apiInfoMapper.apiInfo(apiRequestParam.apiId());
        if (apiInfoResponse == null) {
            return JSONUtil.toBean(JSONUtil.toJsonStr(ResponseResult.fail("API does not exist")), Map.class);
        }
        String method = apiInfoResponse.getApiMethod();
        Map<String,Object> result = null;
        String url = null;
        if (StrUtil.isNotBlank(apiInfoResponse.getEndpoint())){
            url = "https://"+apiInfoResponse.getEndpoint() + "/" + apiInfoResponse.getApiPath();
        }else{
            url = "http://" + apiInfoResponse.getApiHost() +":"+apiInfoResponse.getApiPort() + "/" + apiInfoResponse.getApiPath();
        }
        if (method.equals("POST")) {
            result = httpUtil.post(url,apiRequestParam.params(),apiRequestParam.headers());
        } else if (method.equals("GET")) {
            result = httpUtil.get(url,apiRequestParam.params(),apiRequestParam.headers());
        }
        return result;
    }
}
