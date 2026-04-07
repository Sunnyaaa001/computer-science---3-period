package com.whs.apiplatform.common.oauth.service;

import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import com.whs.apiplatform.common.oauth.domain.ClientUserAuth;
import com.whs.apiplatform.common.oauth.domain.UserInfo;
import com.whs.apiplatform.common.oauth.mapper.ClientPlatformMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.security.oauth2.client.authentication.OAuth2AuthenticationToken;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class OauthService {

    private final ClientPlatformMapper clientPlatformMapper;
    private final SnowflakeIdUtil snowflakeIdUtil;

    public UserInfo findUser(OAuth2AuthenticationToken token) {
        String platformName = token.getAuthorizedClientRegistrationId();
        OAuth2User oAuth2User = token.getPrincipal();
        String subId = oAuth2User.getName();
        String email = oAuth2User.getAttribute("email");
        return clientPlatformMapper.findUserInfoByPlatform(platformName,subId,email);
    }

    @Transactional
    public UserInfo insertUserInfo(OAuth2AuthenticationToken token) {
        String platformName = token.getAuthorizedClientRegistrationId();
        OAuth2User oAuth2User = token.getPrincipal();
        String subId = oAuth2User.getName();
        String email = oAuth2User.getAttribute("email");
        String username = oAuth2User.getAttribute("name");
        UserInfo userInfo = new UserInfo();
        userInfo.setId(snowflakeIdUtil.getId());
        userInfo.setUsername(username);
        userInfo.setEmail(email);
        userInfo.setStatus('0');
        // insert client user
        clientPlatformMapper.insertUserInfo(userInfo);
        //insert client_user_auth
        ClientUserAuth clientUserAuth = new ClientUserAuth();
        clientUserAuth.setId(snowflakeIdUtil.getId());
        clientUserAuth.setUserId(userInfo.getId());
        clientUserAuth.setPlatformType(platformName);
        clientUserAuth.setSubId(subId);
        clientPlatformMapper.insertClientUserAuth(clientUserAuth);
        return userInfo;
    }

    public String getTargetUrl(String platformName) {
        return clientPlatformMapper.getTargetUrl(platformName);
    }
}
