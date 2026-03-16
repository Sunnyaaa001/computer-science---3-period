<script lang="ts" src="../../service/login.ts"></script>

<template>
    <div class="login-page">
        <div class="login-card">
            <h2>API platform</h2>
            <form @submit.prevent = "submitHandle">
                <div class="form-group">
                    <label>Username:
                        <input 
                    type="text"
                    v-model="username"
                    placeholder="please enter your username"/>
                    </label>    
                </div>
                <div class="form-group">
                    <label>Password:
                        <input
                       type="password"
                       v-model="password"
                       placeholder="please enter your password"/></label>
                    
                </div>
                <button type="submit">{{isLogin? 'login':'sign up'}}</button>
                <p class="sign-up-link" @click="isLogin = !isLogin">
                    {{ isLogin ? "Don't have an account? Sign up" : "Already have an account? Login" }}
                </p>
                <p v-if="error" class="error">{{ error }}</p>
            </form>
        </div>
    </div>
</template>

<style lang="css" src="../../assets/css/login.css"></style>