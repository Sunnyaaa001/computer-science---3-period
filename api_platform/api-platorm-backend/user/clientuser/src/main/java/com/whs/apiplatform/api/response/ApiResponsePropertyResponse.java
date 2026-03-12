package com.whs.apiplatform.api.response;

import com.whs.apiplatform.common.tree.TreeNode;
import lombok.Data;

import java.util.Date;
import java.util.List;

@Data
public class ApiResponsePropertyResponse implements TreeNode<ApiResponsePropertyResponse> {

    private Long id;
    private Long apiId;
    private Long parentId;
    private String propertyName;
    private String dataType;
    private String example;
    private Date createTime;
    private Date updateTime;

    private List<ApiResponsePropertyResponse> children;
}
