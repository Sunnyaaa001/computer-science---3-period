package com.whs.apiplatform.user.service;

import com.whs.apiplatform.common.response.ResponseResult;
import com.whs.apiplatform.user.request.LoginUser;
import com.whs.apiplatform.user.request.RegisterUser;

import java.util.Map;

public interface IUserService {

    public ResponseResult<Void> register(RegisterUser registerUser);

    public ResponseResult<Map<String,String>> login(LoginUser loginUser);

    public ResponseResult<Void> logout();
}
