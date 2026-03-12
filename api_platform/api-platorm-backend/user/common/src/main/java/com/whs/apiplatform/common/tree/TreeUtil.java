package com.whs.apiplatform.common.tree;

import cn.hutool.core.util.ObjectUtil;
import org.springframework.util.CollectionUtils;

import java.util.ArrayList;
import java.util.List;

public class TreeUtil {

    public static <T extends TreeNode> List<T> buildTree(List<T> dataList,Long rootId) {
        if(CollectionUtils.isEmpty(dataList) || ObjectUtil.isEmpty(rootId)){
            return new ArrayList<>();
        }
        //get root list
        List<T> rootList = dataList.stream().filter(node -> node.getParentId().equals(rootId)).toList();
        for(T node : rootList){
            node.setChildren(getChildren(node,dataList));
        }
        return rootList;
    }

    public static <T extends TreeNode> List<T> getChildren(T node,List<T> dataList) {
        List<T> children = dataList.stream().filter(item-> item.getParentId().equals(node.getId())).toList();
        if(CollectionUtils.isEmpty(children)){
            return new ArrayList<>();
        }
        for(T child : children){
            node.setChildren(children);
            getChildren(child,dataList);

        }
        return children;
    }
}
