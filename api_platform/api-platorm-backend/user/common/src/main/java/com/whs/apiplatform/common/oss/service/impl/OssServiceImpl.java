package com.whs.apiplatform.common.oss.service.impl;

import cn.hutool.core.lang.UUID;
import com.whs.apiplatform.common.oss.service.IOssService;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.core.sync.ResponseTransformer;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.DeleteObjectRequest;
import software.amazon.awssdk.services.s3.model.DeleteObjectResponse;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.services.s3.presigner.model.GetObjectPresignRequest;
import software.amazon.awssdk.services.s3.presigner.model.PresignedGetObjectRequest;

import java.io.IOException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.time.Duration;

@Service
@RequiredArgsConstructor
public class OssServiceImpl implements IOssService {

    private final S3Client s3Client;

    private final S3Presigner s3Presigner;

    @Override
    public String upload(MultipartFile file, String bucketName, String folder) {
        try {
            String originalFilename = file.getOriginalFilename();
            String extension = originalFilename.substring(originalFilename.lastIndexOf("."));
            String filePath = folder + UUID.randomUUID() + "." + extension;
            s3Client.putObject(
                    builder -> builder.bucket(bucketName)
                            .key(filePath)
                            .contentType(file.getContentType())
                            .build(),
                    RequestBody.fromInputStream(file.getInputStream(), file.getSize())
            );
            return filePath;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public String preview(String bucketName, String filePath) {
        GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                .bucket(bucketName)
                .key(filePath)
                .responseContentDisposition("inline")
                .build();
        GetObjectPresignRequest getObjectPresignRequest = GetObjectPresignRequest.builder()
                .signatureDuration(Duration.ofMinutes(60))
                .getObjectRequest(getObjectRequest)
                .build();
        PresignedGetObjectRequest presignedGetObjectRequest = s3Presigner.presignGetObject(getObjectPresignRequest);
        String url = presignedGetObjectRequest.url().toString();
        return url;
    }

    @Override
    public void download(String bucketName, String filePath, HttpServletResponse response) {
        try {
            String fileName = filePath.substring(filePath.lastIndexOf("/") + 1);
            String encoderName = URLEncoder.encode(fileName, StandardCharsets.UTF_8).replaceAll("\\+", "%20");
            String contentDisposition = String.format("attachment; filename=\"%s\"; filename*=UTF-8''%s",
                    fileName, encoderName);
            response.setContentType("application/octet-stream");
            response.setHeader("Content-Disposition", contentDisposition);
            s3Client.getObject(GetObjectRequest.builder()
                    .bucket(bucketName)
                    .key(filePath)
                    .build(),
                    ResponseTransformer.toOutputStream(response.getOutputStream())
            );
            response.flushBuffer();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Boolean delete(String bucketName, String filePath) {
        DeleteObjectRequest deleteObjectRequest = DeleteObjectRequest.builder()
                .bucket(bucketName)
                .key(filePath).build();
        DeleteObjectResponse deleteObjectResponse = s3Client.deleteObject(deleteObjectRequest);
        return deleteObjectResponse.sdkHttpResponse().isSuccessful();
    }
}
