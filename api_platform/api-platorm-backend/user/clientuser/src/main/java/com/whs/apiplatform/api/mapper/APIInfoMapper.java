package com.whs.apiplatform.api.mapper;

import com.whs.apiplatform.api.response.ApiInfoResponse;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface APIInfoMapper {

    ApiInfoResponse apiInfo(Long apiId);

    List<ApiInfoResponse> apiList(Long categoryId);

    List<ApiInfoResponse> selectApiListByCategoryName(String categoryName);

    ApiInfoResponse apiInfoByName(String apiName);
}
