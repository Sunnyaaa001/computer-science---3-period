package com.whs.apiplatform.api.service;

import com.whs.apiplatform.api.domain.APICategory;
import com.whs.apiplatform.api.request.CategoryParam;
import com.whs.apiplatform.api.response.ApiCategoryResponse;

import java.util.List;

public interface IAPICategoryService {

    public List<ApiCategoryResponse> categoryList(String categoryName);
}
