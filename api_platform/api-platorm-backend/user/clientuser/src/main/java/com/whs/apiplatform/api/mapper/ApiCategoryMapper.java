package com.whs.apiplatform.api.mapper;

import com.whs.apiplatform.api.domain.APICategory;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface ApiCategoryMapper {

    List<APICategory> categoryList(String categoryName);
}
