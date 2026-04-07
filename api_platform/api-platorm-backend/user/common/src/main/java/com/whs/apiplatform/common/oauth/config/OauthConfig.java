package com.whs.apiplatform.common.oauth.config;

import com.whs.apiplatform.common.oauth.domain.ClientPlatform;
import com.whs.apiplatform.common.oauth.mapper.ClientPlatformMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.security.config.oauth2.client.CommonOAuth2Provider;
import org.springframework.security.oauth2.client.registration.ClientRegistration;
import org.springframework.security.oauth2.client.registration.ClientRegistrationRepository;
import org.springframework.security.oauth2.client.registration.InMemoryClientRegistrationRepository;

import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

@Configuration
@RequiredArgsConstructor
public class OauthConfig {

    private final ClientPlatformMapper clientPlatformMapper;

    @Bean
    @Primary
    public ClientRegistrationRepository clientRegistrationRepository(){
        List<ClientPlatform> clientPlatforms = clientPlatformMapper.platformList();
        List<ClientRegistration> registrations = clientPlatforms.stream().map(this::clientRegistration).filter(Objects::nonNull).collect(Collectors.toList());
        return new InMemoryClientRegistrationRepository(registrations);
    }


    private ClientRegistration clientRegistration(ClientPlatform clientPlatform){
        String registrationId = clientPlatform.getPlatformName().trim().toLowerCase();
        String platformName = clientPlatform.getPlatformName().trim().toUpperCase();
        String[] scopes = clientPlatform.getScope().split(",");
        return CommonOAuth2Provider.valueOf(platformName)
                .getBuilder(registrationId)
                .clientId(clientPlatform.getClientId())
                .clientSecret(clientPlatform.getClientSecret())
                .redirectUri("{baseUrl}" + clientPlatform.getAuthorizedRedirectUrl())
                .userNameAttributeName(clientPlatform.getUsernameAttributeName())
                .scope(scopes).build();
    }
}
