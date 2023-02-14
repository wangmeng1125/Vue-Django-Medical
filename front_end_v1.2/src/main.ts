import { createApp } from 'vue'
import App from './App.vue'
import {initRouter} from './router'
import {initStore} from './store'


const app = createApp(App)

// app.use(router)

// 初始化路由
initRouter(app)
// 初始化Vuex
initStore(app)
app.mount('#app')
