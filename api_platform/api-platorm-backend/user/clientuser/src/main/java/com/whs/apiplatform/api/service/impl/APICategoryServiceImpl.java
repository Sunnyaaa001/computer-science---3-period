package com.whs.apiplatform.api.service.impl;

import com.whs.apiplatform.api.mapper.ApiCategoryMapper;
import com.whs.apiplatform.api.response.ApiCategoryResponse;
import com.whs.apiplatform.api.service.IAPICategoryService;
import com.whs.apiplatform.common.tree.TreeUtil;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class APICategoryServiceImpl implements IAPICategoryService {

    private final ApiCategoryMapper apiCategoryMapper;

    @Override
    public List<ApiCategoryResponse> categoryList(String categoryName) {
        List<ApiCategoryResponse> apiCategoryResponses = apiCategoryMapper.categoryList(categoryName);
        List<ApiCategoryResponse> result = TreeUtil.buildTree(apiCategoryResponses,0l);
        return result;
    }
}
