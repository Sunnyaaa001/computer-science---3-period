import type { BasicResponse } from "@/types/basicresponse"

export class LoginUser {
    private username:string
    private password:string

    constructor(username:string,password:string){
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
}

interface LoginData{
    token:string
}

export type LoginResponse = BasicResponse<LoginData>