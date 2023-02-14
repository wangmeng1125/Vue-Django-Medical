import {createStore} from 'vuex'
import type { App } from 'vue'

// 定义key的接口约束 也就是MenuObj
interface MenuObj {
  parentId:number;
  id:number;
  children?:MenuObj[];
  // 上面的这个children注意有可能是一个二级标题还套着一个三级标题
  // 所以这里不知道children是否为空，所以加一个？
}

// 创建菜单接口
interface State {
  menus:MenuObj[]
}

// 创建新的菜单的接口，因为没有对id的类型进行约束，所以我们直接写在外面
interface NewMenus {
  [key:number]:MenuObj
}


// 创建store实例
const store = createStore<State>({ // 注意这个函数调用时，我们一定要写泛型
  state() { 
    return{
      // 因为要存储信息，我们通过定义一个变量来存储
      // 也就是数据都会存储在这个menu中,而且都是以对象的形式存储
      menus:[
        // 这里的是写死的假数据，用来测试的
          {"id": 666,"title": "用户", "level": 0,"sort":0,"parentId":0, "hidden":0},
          {"id": 1,"title": "员工", "password": "123", "level":1,"parentId":666,"hidden":0}, 
          {"id": 2,"title": "经理", "password": "123", "level":1,"parentId":666,"hidden":0}, 
          {"id": 3,"title": "老板", "password": "123", "level":1,"parentId":666,"hidden":0},
          {"id": 4,"title": "算法模型", "level": 0,"sort":0,"parentId":0, "hidden":0},
          {"id": 5,"title": "模型训练", "level": 1,"sort":0,"parentId":4, "hidden":0},
          {"id": 6,"title": "算法测试", "level": 1,"sort":0,"parentId":4, "hidden":0},
      ]

    }
  },
  // 处理vuex中不能直接使用的数据，这个和计算属性挺像的，因为也有缓存机制
  getters:{
    // 获取新的Menus 
    getNewMenus(state){
      console.log("触发。。。。")
      // 使用数组的方式获取菜单
      // const newMenus = [];

      // 使用对象的方式获取菜单
      const newMenus:NewMenus = {};
      // 获取旧的菜单menus
      const menus = state.menus;

      // 循环遍历菜单中的数据 , 并将他们存储到一个新的数组中：为了我们的一二级菜单服务
      for(let i = 0; i<menus.length; i++){

        // 因为算法的存储方式还没设计好，所以直接简单测试一下
        // 如果parentId值为0则是一级标题，否则为二级标题
        if(menus[i].parentId === 0){

          // 一级菜单对象
          // 这里注意是引用的话，每次循环都会直接修改state的menu
          // 而且menus中的数据都是简单类型，所以我们使用浅拷贝
          newMenus[menus[i].id] = { ... menus[i] , children:newMenus[menus[i].id]?.children || []}
        }else{
          
          // 二级菜单 - 对应的一级菜单的ID
          let parentId = menus[i].parentId

          // 我们要确保当传输过来的第一个为二级菜单的时候newMenus是一个对象，空的也行
          newMenus[parentId] = newMenus[parentId] || {} ;

          // 现在我们可以用ParentID获取一级菜单的对象了
          // 确保我们的children是存在的，因为后面要进行一个push操作
          // 如果一开始没有，我们会默认给一个空数组
          newMenus[parentId].children = newMenus[parentId].children || [];
          
          // 将对应的二级菜单push到menus中
          newMenus[parentId].children?.push(menus[i]);
        }
      }
      return newMenus
    }
  },
  // 可以定义修改state方法
  mutations:{
    // 更新菜单
    updateMenus(state, menus){
      state.menus = menus
    }
  },
  // 处理异步操作
  actions:{},
  modules:{},

})

// 导出方法
export const initStore =(app:App<Element>) => {
  // 将我们的路由传入进来
  app.use(store)
}

// export default store;