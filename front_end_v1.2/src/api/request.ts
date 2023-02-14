// export {}
import axios from 'axios'
import { ElMessageBox, ElMessage } from 'element-plus'

// 创建axios实例
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api', // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  // withCredentials：true，//跨域请求时发送cookie
  timeout: 5000 // request timeout
});

// 请求拦截器
instance.interceptors.request.use(config => {
  return config
}, err => {
  console.log(err) // for debug
  return Promise.reject(err)
})

instance.interceptors.response.use(result => {

  return result.data
}, err => {
console.log(err) // for debug
  return Promise.reject(err)
})


  // 【1】
  // 在发送请求之前做一些事情
  // config.headers = config.headers || {}
  // if (localStorage.getItem('token')) {
  //   config.headers.token = localStorage.getItem('token') || ''
  // }
  // 【2】
  // 在发送请求之前做一些事情
  // config.headers = config.headers || {}
  // if (localStorage.getItem('token')) {
  //   config.headers.token = localStorage.getItem('token') || ''
  // }



//请求拦截器：携带的token字段
// service.interceptors.request.use(
//   config => {
//     // 在发送请求之前做一些事情
//     config.headers = config.headers || {}
//     if (localStorage.getItem('token')) {
//       config.headers.token = localStorage.getItem('token') || ''
//     }
//     return config
//   },
//   error => {
//     // do something with request error
//     console.log(error) // for debug
//     return Promise.reject(error)
//   }
// )

//响应拦截器
// service.interceptors.response.use(
//   response => {
//     //服务器响应失败在干什么,因为咱们真实服务器返回code  20000也有可能200
//     if (response.status !== 201 && response.status != 200) {
//       ElMessage({
//         message: response.statusText || 'Error',
//         type: 'error',
//         duration: 5 * 1000
//       })

//       // 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
//       if (response.status === 404 || response.status === 50012 || response.status === 50014) {
//         // to re-login
//         ElMessageBox.confirm('您已注销，您可以取消以保留此页面，或再次登录', '确认注销', {
//           confirmButtonText: 'Re-Login',
//           cancelButtonText: 'Cancel',
//           type: 'warning'
//         }).then(() => {
//           localStorage.dispatch('user/resetToken').then(() => {
//             location.reload()
//           })
//         })
//       }
//       return ''
//     } else {
//       //服务器相应成功干什么
//       return response
//     }
//   },
//   error => {
//     console.log('err' + error) // for debug
//     ElMessage({
//       message: error.message,
//       type: 'error',
//       duration: 5 * 1000
//     })
//     return Promise.reject(error)
//   }
// )

export default instance
