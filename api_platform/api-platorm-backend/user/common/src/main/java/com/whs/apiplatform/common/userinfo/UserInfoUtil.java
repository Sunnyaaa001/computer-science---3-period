package com.whs.apiplatform.common.userinfo;

import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;

import java.util.ArrayList;
import java.util.Map;

public class UserInfoUtil {

    public static void setCurrentUserInfo(Map<String,Object> userInfo){
        UsernamePasswordAuthenticationToken auth = new UsernamePasswordAuthenticationToken(userInfo,null,new ArrayList<>());
        SecurityContextHolder.getContext().setAuthentication(auth);
    }

    public static Map<String,Object> getCurrentUserInfo(){
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        Object principal = authentication.getPrincipal();
        if(principal instanceof Map){
            return (Map<String,Object>)principal;
        }
        return null;
    }

    public static void cleanUserInfo(){
        SecurityContextHolder.clearContext();
    }
}
