package com.whs.apiplatform.api.service.impl;

import com.whs.apiplatform.api.mapper.APIInfoMapper;
import com.whs.apiplatform.api.response.ApiInfoResponse;
import com.whs.apiplatform.api.response.ApiResponsePropertyResponse;
import com.whs.apiplatform.api.service.IAPIInfoService;
import com.whs.apiplatform.common.response.ResponseResult;
import com.whs.apiplatform.common.tree.TreeUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class APIInfoServiceImpl implements IAPIInfoService {

    private final APIInfoMapper apiInfoMapper;

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
}
