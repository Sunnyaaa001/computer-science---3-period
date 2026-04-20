package com.whs.apiplatform.common.oss.config;


import jakarta.servlet.MultipartConfigElement;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.web.servlet.MultipartConfigFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.util.unit.DataSize;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;

import java.net.URI;
import java.net.URISyntaxException;

@Configuration
public class OssConfig {

    @Value("${oss.endpoint}")
    private String endpoint;
    @Value("${oss.accessKey}")
    private String accessKey;
    @Value("${oss.secretKey}")
    private String secretKey;

    @Bean
    public S3Client s3Client() throws URISyntaxException {
        return S3Client.builder()
                .endpointOverride(new URI(endpoint))
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create(accessKey,secretKey)
                ))
                .region(Region.EU_CENTRAL_1)
                .serviceConfiguration(S3Configuration.builder().pathStyleAccessEnabled(Boolean.TRUE).build())
                .build();
    }


    @Bean
    public S3Presigner s3Presigner() throws URISyntaxException {
        return S3Presigner.builder()
                .endpointOverride(new URI(endpoint))
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create(accessKey, secretKey)
                ))
                .region(Region.EU_CENTRAL_1)
                .serviceConfiguration(S3Configuration.builder().pathStyleAccessEnabled(true).build())
                .build();
    }
}
