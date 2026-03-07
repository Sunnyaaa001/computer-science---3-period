package com.whs.apiplatform.common.exceptions;

import com.whs.apiplatform.common.response.ResponseResult;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {
    // handle Method argument validation Exception
    @ExceptionHandler(MethodArgumentNotValidException.class )
    public ResponseResult handleValidationException(MethodArgumentNotValidException exception)
    {
        String message = exception.getBindingResult().getFieldError().getDefaultMessage();
        return ResponseResult.fail(400,message);
    }
    // handle business exception
    @ExceptionHandler(BusinessException.class)
    public  ResponseResult handleBusinessException(BusinessException exception)
    {
        String message = exception.getMessage();
        return ResponseResult.fail(exception.getCode(),message);
    }
}
