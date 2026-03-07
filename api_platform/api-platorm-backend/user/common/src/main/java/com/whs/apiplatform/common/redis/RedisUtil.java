package com.whs.apiplatform.common.redis;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;

import java.util.concurrent.TimeUnit;

@Component
public class RedisUtil {

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    public void set(String key,Object value ){
        redisTemplate.opsForValue().set(key,value);
    }

    public Object get(String key){
        return redisTemplate.opsForValue().get(key);
    }
    public void set(String key,Object value ,long expireTime){
        redisTemplate.opsForValue().set(key,value,expireTime, TimeUnit.SECONDS);
    }
    public Boolean delete(String key){
        return redisTemplate.delete(key);
    }
    public void set_Set(String key,Object... value){
        redisTemplate.opsForSet().add(key,value);
    }
    public Boolean check_set_content(String key,Object value){
        return redisTemplate.opsForSet().isMember(key,value);
    }
    public void remove_content_set(String key,Object value){
        redisTemplate.opsForSet().remove(key,value);
    }
    public Boolean check_exist(String key){
        return redisTemplate.hasKey(key);
    }
}
