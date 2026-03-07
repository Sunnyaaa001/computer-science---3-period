package com.whs.apiplatform;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan("com.whs")
public class platformApplication {
    public static void main(String[] args) {
        SpringApplication.run(platformApplication.class, args);
        System.out.println("API Platform Application Started");
    }
}
