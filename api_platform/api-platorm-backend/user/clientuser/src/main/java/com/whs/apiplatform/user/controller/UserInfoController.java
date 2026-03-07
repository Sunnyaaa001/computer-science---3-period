package com.whs.apiplatform.user.controller;

import com.whs.apiplatform.common.response.ResponseResult;
import com.whs.apiplatform.user.request.LoginUser;
import com.whs.apiplatform.user.request.RegisterUser;
import com.whs.apiplatform.user.service.IUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/client/user")
public class UserInfoController {

    @Autowired
    private IUserService userService;

    @PostMapping("/register")
    public ResponseResult register(@Validated @RequestBody RegisterUser registerUser){
        return userService.register(registerUser);
    }

    @PostMapping("/login")
    public ResponseResult login(@Validated @RequestBody LoginUser loginUser){
        return userService.login(loginUser);
    }

    @GetMapping("/logout")
    public ResponseResult logout(){
        return userService.logout();
    }
}
