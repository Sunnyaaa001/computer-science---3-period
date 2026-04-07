package com.whs.apiplatform.common.filter;

import com.whs.apiplatform.common.oauth.component.OauthSuccessHandler;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.oauth2.client.registration.ClientRegistrationRepository;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfig {

    private final ApiFilter apiFilter;
    private final JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;
    private final ClientRegistrationRepository clientRegistrationRepository;
    private final OauthSuccessHandler oauthSuccessHandler;


    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.csrf(csrf -> csrf.disable())
                .formLogin(formLogin -> formLogin.disable())
                .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED))
                .httpBasic(httpBasic -> httpBasic.disable())
                .securityContext(c -> c.requireExplicitSave(false))
                .exceptionHandling(exceptionHandling -> exceptionHandling.authenticationEntryPoint(jwtAuthenticationEntryPoint))
                .authorizeHttpRequests(auth -> {
                    auth.requestMatchers(
                            "/client/user/login",
                            "/client/user/register",
                            "/login/**",
                            "/oauth2/**",
                            "/test"
                    ).permitAll();
                    auth.requestMatchers("/**/*.css", "/**/*.js", "/webjars/**").permitAll();
                    auth.anyRequest().authenticated();
                })
                        .oauth2Login(oauth ->
                                oauth.clientRegistrationRepository(clientRegistrationRepository)
                                        .successHandler(oauthSuccessHandler));
        http.addFilterBefore(apiFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
