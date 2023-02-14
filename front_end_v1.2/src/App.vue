<template>
  <!-- 这是一个全局组件(目前已经注册了全局组件) -->
  <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<style lang="less">
// 设置一个通配符使得所有的样式都可以初始化
@import url("./assets/styles/rebase.less");

// 设置头部和菜单、菜单右侧的height 100%
html,
body {
  height: 100%;
}
#app {
  height: 100%;
}
</style>
