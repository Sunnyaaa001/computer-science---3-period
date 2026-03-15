package com.whs.apiplatform.api.controller;


import com.whs.apiplatform.api.response.ApiCategoryResponse;
import com.whs.apiplatform.api.response.ApiInfoResponse;
import com.whs.apiplatform.api.service.IAPICategoryService;
import com.whs.apiplatform.api.service.IAPIInfoService;
import com.whs.apiplatform.common.response.ResponseResult;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Objects;

@RestController
@RequestMapping("/client/api")
@RequiredArgsConstructor
public class APIInfoController {


    private final IAPIInfoService apiInfoService;

    private final IAPICategoryService categoryService;


    @GetMapping("/apiInfo/{id}")
    public ResponseResult<ApiInfoResponse> apiInfo(@PathVariable("id") Long apiId){
        return apiInfoService.apiInfo(apiId);
    }

    @GetMapping("/apiInfo/list")
    public ResponseResult<List<ApiInfoResponse>> apiInfoList(Long categoryId){
        List<ApiInfoResponse> apiList = apiInfoService.apiInfoList(categoryId);
        return ResponseResult.success(apiList);
    }

    @GetMapping("/categoryList")
    public ResponseResult<List<ApiCategoryResponse>> categoryList(String categoryName){
        List<ApiCategoryResponse> result = categoryService.categoryList(categoryName);
        return ResponseResult.success(result);
    }

    @PostMapping("/requestAPI")
    public Map<String, Object> requestAPI(){
        return null;
    }
}
