package com.whs.apiplatform.api.controller;


import com.whs.apiplatform.api.response.ApiInfoResponse;
import com.whs.apiplatform.api.service.IAPIInfoService;
import com.whs.apiplatform.common.response.ResponseResult;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/client/api")
@RequiredArgsConstructor
public class APIInfoController {


    private final IAPIInfoService apiInfoService;


    @GetMapping("/apiInfo/{id}")
    public ResponseResult<ApiInfoResponse> apiInfo(@PathVariable("id") Long apiId){
        return apiInfoService.apiInfo(apiId);
    }

    @GetMapping("/apiInfo/list")
    public ResponseResult<List<ApiInfoResponse>> apiInfoList(Long categoryId){
        List<ApiInfoResponse> apiList = apiInfoService.apiInfoList(categoryId);
        return ResponseResult.success(apiList);
    }
}
