package com.whs.apiplatform.common.oauth.mapper;

import com.whs.apiplatform.common.oauth.domain.ClientPlatform;
import com.whs.apiplatform.common.oauth.domain.ClientUserAuth;
import com.whs.apiplatform.common.oauth.domain.UserInfo;
import com.whs.apiplatform.common.oauth.response.ClientPlatformResponse;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface ClientPlatformMapper {

    List<ClientPlatformResponse> selectAllClientPlatform();

    List<ClientPlatform> platformList();

    UserInfo findUserInfoByPlatform(@Param("platformName") String platformName, @Param("subId") String subId,@Param("email")  String email);

    int insertUserInfo(UserInfo userInfo);

    int insertClientUserAuth(ClientUserAuth clientUserAuth);

    String getTargetUrl(@Param("platformName") String platformName);
}
