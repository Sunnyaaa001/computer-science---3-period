import type { BasicResponse } from "@/types/basicresponse"

export class LoginUser {
    private username:string
    private password:string

    constructor(username:string = "",password:string = ""){
        this.username=username
        this.password=password
    }

    getusername():string{
        return this.username
    }
    
    getpassword():string{
        return this.password
    }

    setUsername(username:string){
        this.username = username
    }

    setPassword(password:string){
        this.password = password
    }

    async login():Promise<{httpSatus:number;data:LoginResponse}>{
        const response = await fetch("/system/user/login",{
            method :"POST",
            headers:{"Content-type":"application/json"},
            body:JSON.stringify({
                username:this.username,
                password:this.password
            })
        })
        const data:LoginResponse = await response.json()
        return {httpSatus:response.status,data}
    }

    async signUp():Promise<{httpsSatus:number,data:BasicResponse}> {
        const response = await fetch("/system/user/register",{
            method:"POST",
            headers:{"Content-type":"application/json"},
            body:JSON.stringify({
                 username:this.username,
                 password:this.password
            })
        })
        const data = await response.json()
        return {httpsSatus:response.status,data}
    }

    async logout(token:string):Promise<{httpStatus:number,data:BasicResponse}> {
        const response = await fetch(
            "/system/user/logout",{
                method:"GET",
                headers:{
                    "Authorization":token
                }
            }
        );
        const data = await response.json()
        return {httpStatus:response.status,data:data}
    }
}

interface LoginData{
    token:string
}

export type LoginResponse = BasicResponse<LoginData>