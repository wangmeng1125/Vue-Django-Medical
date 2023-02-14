<template>
  <div>主界面</div>
</template>

<script lang="ts">
import { reactive, defineComponent, onMounted, toRefs, ref } from "vue";
import { ElMessage } from "element-plus";
import {
  reqUserList,
  reqUserListOne,
  reqDeleteUser,
  // reqAddOrUpdateUser,
} from "../api/user";

export default defineComponent({
  setup() {
    // 【1】用户状态数据
    const state = reactive({
      user_list: [],
      index: 0,
      user_id: "",
      form: {
        name: "",
        password: "",
        age: 0,
      },
    });

    // 【2】查询所有用户的信息
    const getList = () => {
      reqUserList().then((res) => {
        console.log(res);
        state.user_list = res.data;
      });
    };

    // 【3】删除用户
    // 删除
    const handleDelete = (index: number, row: any) => {
      reqDeleteUser(index + 1).then((res) => {
        if (res.status == 200) {
          // 调用饿了么的弹窗提醒
          ElMessage({ type: "success", message: "删除成功" });
          // 重新加载列表
          getList();
        }
      });
    };

    // 如果我们想当加载这个页面的时候直接发送请求
    // 可以使用生命周期中自带的（初始挂载）
    // 初始挂载，自带
    onMounted(() => {
      getList();
    });
    return {};
  },
});
</script>

<style scoped>
</style>