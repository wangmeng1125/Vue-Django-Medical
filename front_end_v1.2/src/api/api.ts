import request from './request'

// return request({url: `/App/${id}`, method: `get`})


// 使用类型别名或者接口名
// 注意：接口名可以重复， 但是类型别名是不能重复的
// 类型别名是可以使用:联合类型、交叉类型
type PromiseRes<T> = Promise<ManageResult<T>>



// 【interface】<================>登录参数接口
interface AdminLoginData {
  "username": string
  "password": string
}

// 【interface】<================>所有接口的泛型
interface ManageResult<T> {
  code:number;
  data:T;
}

// 【interface】<================>Res接口 改边返回值类型 <接口泛型>
interface AdminLoginRes {
    code:number;
    message:string;
  }

// 【interface】<================>当前的用用户信息
// interface AdminInfoRes {
//   menus:[
//   ]
// }

interface AdminInfoRes {
  data:[
    {
      id: number, 
      name: string, 
      password: string, 
      age: number,
    }
  ]
}



// 【POST】<================>登录返回token接口
export const adminLoginApi = (data:AdminLoginData):
  PromiseRes<AdminLoginRes>=> request.post('/App/login/',data);



// 【GET】<================>获取当前登录用户的信息
export const getAdminInfoApi= ():
PromiseRes<AdminInfoRes>=> request.get('/App/user_info')





// 【】<================>登录返回token





// 【】<================>登录返回token

