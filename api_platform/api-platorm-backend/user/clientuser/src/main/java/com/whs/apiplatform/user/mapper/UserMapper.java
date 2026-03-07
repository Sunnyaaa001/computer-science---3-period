package com.whs.apiplatform.user.mapper;


import com.whs.apiplatform.user.domain.UserInfo;
import jakarta.validation.constraints.NotBlank;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper {

    public int addUser(UserInfo user);

    UserInfo selectUserByUsername(String username);
}
