package com.whs.apiplatform.common.filter;

import cn.hutool.core.bean.BeanUtil;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.whs.apiplatform.common.redis.RedisUtil;
import com.whs.apiplatform.common.response.ResponseResult;
import com.whs.apiplatform.common.token.TokenUtil;
import com.whs.apiplatform.common.userinfo.UserInfoUtil;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.Map;

@Component
public class ApiFilter extends OncePerRequestFilter {

    private final ObjectMapper objectMapper;
    private final TokenUtil tokenUtil;
    private final RedisUtil redisUtil;
    @Value("${token.redisFolder}")
    private String tokenRedisFolder;
    @Value("${token.time}")
    private Long tokenTime;

    public ApiFilter(ObjectMapper objectMapper, TokenUtil tokenUtil,RedisUtil redisUtil) {
        this.objectMapper = objectMapper;
        this.tokenUtil = tokenUtil;
        this.redisUtil = redisUtil;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        String token = request.getHeader("Authorization");
        if (token == null || !token.startsWith("Bearer ")) {
            filterChain.doFilter(request, response);
            return;
        }
        ResponseResult result = ResponseResult.fail(401, "Invalid Token, Please login again!");
        response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setCharacterEncoding("UTF-8");
        // check token
        token = token.substring(7);
        if (!tokenUtil.validateToken(token)) {
            objectMapper.writeValue(response.getWriter(), result);
            return;
        }
        //parse token
        Map<String, Object> payload = tokenUtil.parseToken(token);
        String key = tokenRedisFolder + ":" + payload.get("id").toString();
        if(!redisUtil.check_exist(key)){
            objectMapper.writeValue(response.getWriter(), result);
            return;
        }
        Object userInfo = redisUtil.get(key);
        redisUtil.set(key,userInfo,tokenTime);
        // put current user into SecurityHolderContext
        Map<String, Object> userMap = BeanUtil.beanToMap(userInfo);
        UserInfoUtil.setCurrentUserInfo(userMap);
        try {
            filterChain.doFilter(request, response);
        }finally {
            UserInfoUtil.cleanUserInfo();
        }
    }
}
