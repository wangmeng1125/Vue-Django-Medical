import { createRouter, createWebHistory, type RouteRecord, type RouteRecordRaw } from 'vue-router'
// import Home from '../views/Home.vue'
// 【Vue3】这个是vue3的路由写法
import type { App } from 'vue';
import { useStore } from 'vuex';
// import Cookies from 'js-cookie'
// import store from '../store'
import {getAdminInfoApi} from '../api/api'

const routes: RouteRecordRaw[] = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/main',
  //   name: 'main',
  //   component: () => import('../views/main.vue')
  // },
  {
    // 登录
    path: '/login',
    name: 'login',
    component: () => import('../views/login/login.vue')
  },
  {
    // 用户页面 homepage
    path: '/homepage',
    name: 'homepage',
    component: () => import('../views/homepage/homepage.vue')
  }

]

// 路由对象
const router = createRouter({ 
  history: createWebHistory(),
  routes // 路由配置
})

// 前置导航守卫
// router.beforeEach((to, form, next) => {
//   // 重新拿到menu数据的条件
//     // 【1】token && vuex里面的menus(权限列表) 为空
//     // const token = Cookies.get('token');
//     if(store.state.menus.length === 0 ){
//       console.log("menus为空");
//       getAdminInfoApi().then(res =>{
//         if (res.code == 200){
//           // 拿到数据我们就要存储到Vuex中 
//           // 将res.data.menus存储进Vuex中
//           store.commit('updateMenus', res.data.menus);
//         }
//       })
//     }

//   // 添加防止死循环的跳转指令(页面的跳转都在这个里面)
//   next();

// })

export const initRouter = (app: App<Element>) => {
  app.use(router);
}


// export default router