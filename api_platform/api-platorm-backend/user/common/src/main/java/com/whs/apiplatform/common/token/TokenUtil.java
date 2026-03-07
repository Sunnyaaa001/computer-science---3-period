package com.whs.apiplatform.common.token;

import cn.hutool.json.JSONObject;
import cn.hutool.jwt.JWT;
import cn.hutool.jwt.JWTPayload;
import cn.hutool.jwt.JWTUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class TokenUtil {

    @Value("${token.secretKey}")
    private String secretKey;


    public String createToken(Map<String,Object> payload) {
        String token = JWTUtil.createToken(payload, secretKey.getBytes());
        return "Bearer " + token;
    }

    public Map<String,Object> parseToken(String token) {
        JWT jwt = JWTUtil.parseToken(token);
        JWTPayload payload = jwt.getPayload();
        JSONObject claims = payload.getClaimsJson();
        return claims.getRaw();
    }

    public Boolean validateToken(String token) {
       return JWTUtil.verify(token,secretKey.getBytes());
    }
}
