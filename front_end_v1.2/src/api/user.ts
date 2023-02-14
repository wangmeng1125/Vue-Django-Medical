// 获取音乐列表的接口
import request from "./request"
// /api/musics
export function reqUserList() {
    return request({url: `/App`, method: `get`})
}

// 查询单个
export function reqUserListOne(id:number) {
    return request({url: `/App/${id}`, method: `get`})
}

// 删除
export function reqDeleteUser(id:number) {
    return request({url: `/App/${id}`, method: `delete`})
}

// 增加或者修改
// export function reqAddOrUpdateUser(user:any, index:number){
//     if (index != 0){
//         return request({url:`App/update/${index}`, method:'put', data:user})
//     }else{
//       //新增品牌
//       return request({ url: '/App', method: 'post', data: user });  
//     }
// }


export function whichOnePeople(){
  return request（{url:'/App',method: 'get'）
}

