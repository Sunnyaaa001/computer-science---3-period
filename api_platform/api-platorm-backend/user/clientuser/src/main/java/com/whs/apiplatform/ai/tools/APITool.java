package com.whs.apiplatform.ai.tools;

import cn.hutool.core.util.StrUtil;
import cn.hutool.json.JSONUtil;
import com.whs.apiplatform.api.mapper.APIInfoMapper;
import com.whs.apiplatform.api.request.APIAIRequestParam;
import com.whs.apiplatform.api.response.ApiCategoryResponse;
import com.whs.apiplatform.api.response.ApiInfoResponse;
import com.whs.apiplatform.api.service.IAPICategoryService;
import com.whs.apiplatform.common.http.HttpUtil;
import com.whs.apiplatform.common.response.ResponseResult;
import dev.langchain4j.agent.tool.P;
import dev.langchain4j.agent.tool.Tool;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

@Component
@RequiredArgsConstructor
public class APITool {

    private final IAPICategoryService categoryService;

    private final APIInfoMapper apiInfoMapper;

    private final HttpUtil httpUtil;

    @Tool("select API category list, the param is category name.")
    public List<ApiCategoryResponse> categoryList(@P("categoryName") String categoryName) {
        return categoryService.categoryList(categoryName);
    }

    @Tool("Call this tool when the user asks for API information or a list of interfaces for a specific category. If the user does not specify a category, pass null as the argument.")
    public List<ApiInfoResponse> apiInfoList(@P("categoryName") String categoryName){
        List<ApiInfoResponse> apiInfoResponses = apiInfoMapper.selectApiListByCategoryName(categoryName);
        return apiInfoResponses;
    }

    @Tool("Call this tool when user want to request API, the API name is required, params and headers are optional")
    public Map<String,Object> requestApiCall(@P("apiName") String apiName,
                                         @P("params") Map<String, Object> params,
                                         @P("headers") Map<String, Object> headers){
        ApiInfoResponse apiInfoResponse = apiInfoMapper.apiInfoByName(apiName);
        if(apiInfoResponse==null){
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
            result = httpUtil.post(url,params,headers);
        } else if (method.equals("GET")) {
            result = httpUtil.get(url,params,headers);
        }
        return result;
    }
}
