package com.whs.apiplatform.common.oss.service;

import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.multipart.MultipartFile;

public interface IOssService {

    String upload(MultipartFile file, String bucketName, String folder);

    String preview(String bucketName, String filePath);

    void download(String bucketName, String filePath, HttpServletResponse response);

    Boolean delete(String bucketName, String filePath);
}
