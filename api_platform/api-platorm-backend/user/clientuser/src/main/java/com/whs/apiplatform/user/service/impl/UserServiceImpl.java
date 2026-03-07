package com.whs.apiplatform.user.service.impl;

import com.whs.apiplatform.common.exceptions.BusinessException;
import com.whs.apiplatform.common.id.SnowflakeIdUtil;
import com.whs.apiplatform.common.redis.RedisUtil;
import com.whs.apiplatform.common.response.ResponseResult;
import com.whs.apiplatform.common.token.TokenUtil;
import com.whs.apiplatform.common.userinfo.UserInfoUtil;
import com.whs.apiplatform.user.domain.UserInfo;
import com.whs.apiplatform.user.mapper.UserMapper;
import com.whs.apiplatform.user.request.LoginUser;
import com.whs.apiplatform.user.request.RegisterUser;
import com.whs.apiplatform.user.service.IUserService;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@Service
public class UserServiceImpl implements IUserService {

    String key = "client_user";

    @Autowired
    private RedisUtil redisUtil;

    @Autowired
    private UserMapper userMapper;
    @Autowired
    private SnowflakeIdUtil snowflakeIdUtil;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private TokenUtil tokenUtil;

    @Value("${token.redisFolder}")
    private String tokenRedisFolder;

    @Value("${token.time}")
    private Long time;

    @Override
    @Transactional
    public ResponseResult<Void> register(RegisterUser registerUser) {
        // check whether username is unique
        if(redisUtil.check_set_content(key,registerUser.username())){
            throw new BusinessException(500,"This account has been registered");
        }
        // add user into database
        UserInfo userInfo = new UserInfo();
        BeanUtils.copyProperties(registerUser,userInfo);
        // encrypt password
        userInfo.setPassword(passwordEncoder.encode(registerUser.password()));
        userInfo.setId(snowflakeIdUtil.getId());
        userInfo.setCreateTime(new Date());
        userInfo.setStatus('0');
        userInfo.setUpdateTime(userInfo.getCreateTime());
        int result = userMapper.addUser(userInfo);
        if(result <= 0){
            return ResponseResult.fail("insert fail!");
        }
        // put username into redis set
        redisUtil.set_Set(key,registerUser.username());
        return ResponseResult.success();
    }

    @Override
    public ResponseResult<Map<String, String>> login(LoginUser loginUser) {
        // check current account whether exists
        if (!redisUtil.check_set_content(key,loginUser.username())){
            throw new BusinessException(500,"This account does not exist!");
        }
        // select current user information by name in the database
        UserInfo userInfo = userMapper.selectUserByUsername(loginUser.username());
        // check the password
        if(!passwordEncoder.matches(loginUser.password(),userInfo.getPassword())){
            throw new BusinessException(500,"username or password incorrect!");
        }
        //generate token
        Map<String,Object> payload = new HashMap<>();
        payload.put("id",userInfo.getId());
        payload.put("signature",snowflakeIdUtil.getId());
        payload.put("timeStamp",new Date().getTime());
        String token = tokenUtil.createToken(payload);
        //put user information into Redis
        redisUtil.set(tokenRedisFolder+":"+userInfo.getId(),userInfo,time);
        // return token to front end
        Map<String,String> result = new HashMap<>();
        result.put("token",token);
        return ResponseResult.success(result);
    }

    @Override
    public ResponseResult<Void> logout() {
        // get current user
        Map<String,Object> userInfo = UserInfoUtil.getCurrentUserInfo();
        //remove user information in the Redis
        redisUtil.delete(tokenRedisFolder+":"+userInfo.get("id"));
        // remove user information in the Application context
        UserInfoUtil.cleanUserInfo();
        return ResponseResult.success();
    }
}
