package com.whs.apiplatform.common.tree;


import java.util.List;

public interface TreeNode<T> {
    Long getId();
    Long getParentId();
    void setChildren(List<T> children);
    List<T> getChildren();
}
