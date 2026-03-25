import { createRouter,createWebHistory,RouteRecordRaw } from "vue-router";
import LoginView from "@/pages/login/login.vue"

const routes:Array<RouteRecordRaw> = [
    {path:"/",redirect:"/login"},
    {path:"/login",component:LoginView},
    {
        path:"/index",
        name:"Index",
        redirect:"/index/home",
        component:()=>import("@/pages/index/index.vue"),
        children:[
            {
                path:"home",
                name:"Home",
                component:()=> import("@/pages/home/home.vue")
            },
            {
                path:"categories",
                name:"Categories",
                component:()=> import("@/pages/categories/categories.vue")
            },
            {
                path:"api",
                name:"Api",
                component:()=>import("@/pages/api/api.vue")
            }
        ]
       }
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router