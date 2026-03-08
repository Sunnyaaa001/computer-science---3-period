package com.whs.apiplatform.ai.tools;

import com.whs.apiplatform.api.domain.APICategory;
import com.whs.apiplatform.api.request.CategoryParam;
import com.whs.apiplatform.api.service.IAPICategoryService;
import dev.langchain4j.agent.tool.Tool;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class APITool {

    @Autowired
    private IAPICategoryService categoryService;

    @Tool("select API category list, the param is category name.")
    public List<APICategory> categoryList(CategoryParam categoryParam) {
        if(categoryParam == null){
            categoryParam = new CategoryParam("");
        }
        return categoryService.categoryList(categoryParam);
    }
}
