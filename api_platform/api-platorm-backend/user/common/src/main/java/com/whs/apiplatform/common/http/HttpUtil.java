package com.whs.apiplatform.common.http;

import lombok.RequiredArgsConstructor;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestClient;
import org.springframework.web.util.UriComponentsBuilder;

import java.util.Map;

@Component
@RequiredArgsConstructor
public class HttpUtil {

    private final RestClient.Builder restClient;


    public Map<String, Object> get(String url,Map<String,Object> params,Map<String,Object> headers) {
        UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl(url);
        if(params != null){
            MultiValueMap<String, String> multiValueMap = new LinkedMultiValueMap<>();
            params.forEach((k, v) -> multiValueMap.add(k, String.valueOf(v)));
            builder.queryParams(multiValueMap);
        }
        return restClient.build()
                .get()
                .uri(builder.build().toUri())
                .headers(httpHeaders -> {
                    if (headers != null){
                        headers.forEach((k,v)->{
                            httpHeaders.add(k,v.toString());
                        });
                    }
                })
                .accept(MediaType.APPLICATION_JSON)
                .retrieve()
                .body(new ParameterizedTypeReference<Map<String, Object>>() {});
    }

    public Map<String, Object> post(String url,Map<String,Object> params,Map<String,Object> headers) {
        UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl(url);
        return restClient.build()
                .post()
                .uri(builder.build().toUri())
                .body(params)
                .headers(httpHeaders -> {
                    if (headers != null) {
                        headers.forEach((k, v) -> httpHeaders.add(k, v.toString()));
                    }
                })
                .accept(MediaType.APPLICATION_JSON)
                .contentType(MediaType.APPLICATION_JSON)
                .retrieve()
                .body(new ParameterizedTypeReference<Map<String, Object>>() {});
    }
}
