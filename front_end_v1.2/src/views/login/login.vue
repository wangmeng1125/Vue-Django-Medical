<!-- ============================= ======= ============================= -->
<!-- ============================= ======= ============================= -->
<!-- ============================= 界面骨架 ============================= -->
<!-- ============================= ======= ============================= -->
<!-- ============================= ======= ============================= -->
<template>
  <h1>医疗大数据平台</h1>

  <el-form
    ref="ruleFormRef"
    :model="ruleForm"
    :rules="rules"
    class="demo-ruleForm"
  >
    <!-- {% csrf_token %} -->
    <!-- 【1】用户名 -->
    <el-form-item prop="username">
      <el-input v-model="ruleForm.username" type="text" autocomplete="off" />
    </el-form-item>
    <!-- 【2】登录密码 -->
    <el-form-item prop="password">
      <el-input
        v-model="ruleForm.password"
        type="password"
        autocomplete="off"
      />
    </el-form-item>
    <!-- 【3】登录按钮 -->
    <el-form-item>
      <el-button type="primary" @click="loginFn()">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<!-- ================================================================= -->
<!-- ================================================================= -->
<!-- =============================业务逻辑============================== -->
<!-- ================================================================= -->
<!-- ================================================================= -->

<script lang='ts' setup>
import { reactive, toRefs, ref, toRef } from "vue";
import { adminLoginApi, getAdminInfoApi } from "../../api/api";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

// <======【1】定义两个属性======>
const state = reactive({
  ruleForm: {
    username: "",
    password: "",
  },
});

// <======【】获取el-form组件对象======>
let ruleFormRef = ref();

// <======【】获取项目路由对象======>
let router = useRouter();

// <======【】获取Vuex对象======>
let store = useStore();

// <======【】定义校验函数======>
const validatePass = (
  rule: unknown,
  value: string | undefined,
  callback: (msg?: string) => void
) => {
  if (value === "") {
    callback("密码不能为空");
  } else {
    callback();
  }
};

// <======【】表单校验规则======>
const rules = reactive({
  // 默认的用户名校验方式
  username: [{ required: true, message: "用户名不能为空", trigger: "blur" }],
  password: [{ validator: validatePass, trigger: "blur" }],
});

// <======【】解构state复用======>
let { ruleForm } = toRefs(state);

// <======【】登录校验函数======>{使用对象属性}
const loginFn = () => {
  // 点击按钮触发表单校验
  ruleFormRef.value.validate().then(() => {
    console.log("校验通过,用户名和密码合法");

    // 发送请求的函数方法
    adminLoginApi({
      username: ruleForm.value.username,
      password: ruleForm.value.password,
    })
      .then((res) => {
        // 通过函数内置的类型重新定义code
        if (res.code == 200) {
          // 成功登录
          console.log("登录成功");
          console.log("正在跳转到用户界面.....");
          // router.push("/homepage");
          console.log("跳转成功！");
          // 这里可以设置存储token值，现在先不弄
          // 而且要注意这里的if里面是异步请求，就是如果放在外面则不能获取token
          // router.push("/homepage");
          // 登录成功，获取当前用户的信息
          getAdminInfoApi().then((res) => {
            // 通过Promise 的形式
            if (res != null) {
              // if (1) {
              // 这样就获取了所有用户的信息
              // res.data.data;
              // 打印用户信息做测试
              console.log(res);
              // 存储用户信息
              store.commit("updateMenus", res);

              // 进行跳转到homepage
              router.push("/homepage");
            }
          });
        }
      })
      .catch(() => {
        console.log("校验不通过");
      });
  });
};

// <======【】d登录校验校验函数======>{传入的是对象}
// const loginFn = () => {
//   ruleFormRef.value
//     .validate()
//     .then(() => {
//       console.log("校验通过,欢迎使用");

//       // 点击登录触发
//       adminLoginApi({
//         name: ruleForm.value.username,
//         password: ruleForm.value.password,
//       });
//     })

//     // 通过返回的状态码校验
//     .then((res: { code: number }) => {
//       if (res.code === 200) {
//         console.log("登录成功");
//       }
//     })
//     .catch(() => {
//       console.log("校验不通过");
//     });
// };

// <======【】定义校验函数======>

// <======【】定义校验函数======>

// <======【】定义校验函数======>

// <======【】定义校验函数======>

// <======【】定义校验函数======>

// <!-- ============================= ======= ============================= -->
// <!-- ============================= ======= ============================= -->
// <!-- ============================= 样式设置 ============================= -->
// <!-- ============================= ======= ============================= -->
// <!-- ============================= ======= ============================= -->
</script>

<style lang="scss" scoped>
</style>


<!-- @click="submitForm('ruleForm')" -->