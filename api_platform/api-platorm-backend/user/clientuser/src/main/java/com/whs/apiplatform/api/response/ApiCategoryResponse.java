package com.whs.apiplatform.api.response;

import com.whs.apiplatform.common.tree.TreeNode;
import lombok.Data;

import java.util.Date;
import java.util.List;

@Data
public class ApiCategoryResponse implements TreeNode<ApiCategoryResponse> {
    private Long id;
    private Long parentId;
    private String categoryName;
    private Integer sort;
    private String ancestors;
    private Long creatorId;
    private Date createTime;
    private Date updateTime;

    private List<ApiCategoryResponse> children;
}
