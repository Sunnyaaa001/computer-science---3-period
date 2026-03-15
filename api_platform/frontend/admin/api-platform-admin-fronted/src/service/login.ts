import { defineComponent, ref } from "vue";
import { LoginUser } from "@/components/auth";

export default defineComponent({
    name:"Login",
    setup(){
        const isLogin = ref<boolean>(true)
        const username = ref<string>("")
        const password = ref<string>("")
        const error = ref<string>("")

        const handleLogin = async () =>{
            if(!username.value || !password.value){
                error.value = "Please enter username and password!"
                return
            }

            try{
         // create LoginUser instance
         const loginUser = new LoginUser(username.value,password.value)
         const response = await loginUser.login()
         if(response.httpSatus != 200 || response.data.code != 200){
            error.value = response.data.message
            return
         }
         localStorage.setItem("Authorization",response.data.data.token)
         //redirect to index.vue
        }catch(error:any){
            console.log("Login failed:",error)
            error.value = "login failed!"
        }
        }

        return {isLogin,username,password,error,handleLogin}
    }
})