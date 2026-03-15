import { createRouter,createWebHistory } from "vue-router";
import LoginView from "@/pages/login/login.vue"

const routes = [
    {path:"/",redirect:"/login"},
    {path:"/login",component:LoginView}
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router