package com.whs.apiplatform.api.service.impl;

import com.whs.apiplatform.api.domain.APICategory;
import com.whs.apiplatform.api.mapper.ApiCategoryMapper;
import com.whs.apiplatform.api.request.CategoryParam;
import com.whs.apiplatform.api.service.IAPICategoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class APICategoryServiceImpl implements IAPICategoryService {

    @Autowired
    private ApiCategoryMapper apiCategoryMapper;

    @Override
    public List<APICategory> categoryList(CategoryParam categoryParam) {
        return apiCategoryMapper.categoryList(categoryParam.categoryName());
    }
}
