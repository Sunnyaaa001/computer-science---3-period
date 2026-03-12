package com.whs.apiplatform.ai.tools;

import com.whs.apiplatform.api.domain.APICategory;
import com.whs.apiplatform.api.mapper.APIInfoMapper;
import com.whs.apiplatform.api.request.CategoryParam;
import com.whs.apiplatform.api.response.ApiInfoResponse;
import com.whs.apiplatform.api.service.IAPICategoryService;
import dev.langchain4j.agent.tool.P;
import dev.langchain4j.agent.tool.Tool;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
@RequiredArgsConstructor
public class APITool {

    private final IAPICategoryService categoryService;

    private final APIInfoMapper apiInfoMapper;

    @Tool("select API category list, the param is category name.")
    public List<APICategory> categoryList(@P("categoryName") String categoryName) {
        return categoryService.categoryList(categoryName);
    }

    @Tool("Call this tool when the user asks for API information or a list of interfaces for a specific category. If the user does not specify a category, pass null as the argument.")
    public List<ApiInfoResponse> apiInfoList(@P("categoryName") String categoryName){
        List<ApiInfoResponse> apiInfoResponses = apiInfoMapper.selectApiListByCategoryName(categoryName);
        return apiInfoResponses;
    }

}
