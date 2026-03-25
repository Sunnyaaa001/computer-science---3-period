import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { LoginUser } from '@/components/auth';


export interface menuItem {
    name:string
    path:string
    icon:string
}

export function useIndex(){
    const route = useRoute()
    const router = useRouter()

    const menuList:menuItem[] = [
        {name:"DashBoard",path:"/index/home",icon:"💎"},
        {name:"API Categories",path:"/index/categories",icon:"📂"},
        {name:"API Information",path:"/index/api",icon:"⚡"}
    ]

    const currentRouteName = computed<string>(() => {
        const activeMenu = menuList.find((menu)=> menu.path == route.path);
        return activeMenu?.name?? 'Overview';
    });

    const handlelogout = async ():Promise<void> => {
        const loginUser = new LoginUser()
        const token:string = localStorage.getItem("Authorization") || ""
        await loginUser.logout(token)
        localStorage.removeItem("Authorization")
        router.push("/login")
    }
    return {currentRouteName,handlelogout,menuList}
}

