package com.whs.apiplatform.common.response;

import lombok.Data;

import java.io.Serializable;

@Data
public class ResponseResult<T> implements Serializable {

    private int code;
    private String message;
    private T data;

    public ResponseResult(int code, String message, T data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }

    public static <T> ResponseResult<T> success(T data) {
        return new ResponseResult<>(200, "success!", data);
    }

    public static <T> ResponseResult<T> success() {
        return success(null);
    }

    public static <T> ResponseResult<T> fail(int code, String message) {
        return new ResponseResult<>(code, message, null);
    }

    public static <T> ResponseResult<T> fail(String message) {
        return fail(500, message);
    }
}
