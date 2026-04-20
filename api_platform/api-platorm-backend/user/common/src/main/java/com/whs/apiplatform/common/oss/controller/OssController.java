package com.whs.apiplatform.common.oss.controller;


import com.whs.apiplatform.common.oss.service.IOssService;
import com.whs.apiplatform.common.response.ResponseResult;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/oss")
@RequiredArgsConstructor
public class OssController {

    private final IOssService ossService;

    @PostMapping("/upload")
    public ResponseResult<String> upload(MultipartFile file,String bucketName,String folder) {
        String url = ossService.upload(file,bucketName,folder);
        return ResponseResult.success(url);
    }

    @GetMapping("/preview")
    public ResponseResult<String> preview(String bucketName,String filePath) {
        String url = ossService.preview(bucketName,filePath);
        return ResponseResult.success(url);
    }

    @GetMapping("/download")
    public void download(String bucketName, String filePath, HttpServletResponse response) {
        ossService.download(bucketName,filePath,response);
    }

    @DeleteMapping("/delete")
    public ResponseResult<String> deleteFile(String bucketName, String filePath){
        if (ossService.delete(bucketName,filePath))
        {
            return ResponseResult.success();
        }else {
            return ResponseResult.fail("delete fail!");
        }
    }
}
