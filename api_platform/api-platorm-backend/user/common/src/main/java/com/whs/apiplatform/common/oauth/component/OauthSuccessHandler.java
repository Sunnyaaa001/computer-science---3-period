package com.whs.apiplatform.common.oauth.component;

import cn.hutool.core.util.ObjectUtil;
import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import com.whs.apiplatform.common.oauth.domain.UserInfo;
import com.whs.apiplatform.common.oauth.service.OauthService;
import com.whs.apiplatform.common.redis.RedisUtil;
import com.whs.apiplatform.common.response.ResponseResult;
import com.whs.apiplatform.common.token.TokenUtil;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.Authentication;
import org.springframework.security.oauth2.client.authentication.OAuth2AuthenticationToken;
import org.springframework.security.web.authentication.AuthenticationSuccessHandler;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@Component
@RequiredArgsConstructor
public class OauthSuccessHandler implements AuthenticationSuccessHandler {

    private final OauthService oauthService;
    private final RedisUtil redisUtil;
    private final TokenUtil tokenUtil;
    private final SnowflakeIdUtil snowflakeIdUtil;
    String key = "client_user";
    @Value("${token.redisFolder}")
    private String tokenRedisFolder;

    @Value("${token.time}")
    private Long time;

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        // get the third platform user information
        OAuth2AuthenticationToken token = (OAuth2AuthenticationToken) authentication;
        UserInfo user = oauthService.findUser(token);
        if(ObjectUtil.isEmpty(user)){
            user = oauthService.insertUserInfo(token);
            //put username into the redis set
            redisUtil.set_Set(key,user.getUsername());
        }
        // generate token
        Map<String,Object> payload = new HashMap<>();
        payload.put("id",user.getId());
        payload.put("signature",snowflakeIdUtil.getId());
        payload.put("timeStamp",new Date().getTime());
        String jwtToken = tokenUtil.createToken(payload);
        //put user information into Redis
        redisUtil.set(tokenRedisFolder+":"+user.getId(),user,time);
        String targetUrl = oauthService.getTargetUrl(token.getAuthorizedClientRegistrationId());
        response.sendRedirect(targetUrl + "?token=" + jwtToken);
    }
}
