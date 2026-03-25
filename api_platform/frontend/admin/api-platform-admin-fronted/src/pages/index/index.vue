<script lang="ts" src="../../service/index.ts"></script>


<template>
  <div class="index-container">
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo-box">API</div>
        <span>Platform</span>
      </div>

      <nav class="menu-list">
        <router-link 
          v-for="item in menuList" 
          :key="item.path" 
          :to="item.path"
          class="menu-item"
        >
          <span class="menu-icon">{{ item.icon }}</span>
          <span class="menu-text">{{ item.name }}</span>
        </router-link>
      </nav>

      <div class="sidebar-footer" @click="handleLogout">
        <span class="logout-btn">Logout</span>
      </div>
    </aside>

    <main class="main-content">
      <header class="top-nav">
        <div class="breadcrumb">Console / {{ currentRouteName }}</div>
        <div class="user-info">
          <span class="status-dot"></span>
          Connected to API
        </div>
      </header>

      <section class="page-view">
        <router-view />
      </section>
    </main>
  </div>
</template>