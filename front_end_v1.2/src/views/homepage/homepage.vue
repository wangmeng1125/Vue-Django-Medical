<template>
  <div class="homepage_container">
    <div class="homepage_header">头部</div>
    <div class="homepage_menu">
      <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"
        default-active="2"
        text-color="#fff"
        @open="handleOpen"
        @close="handleClose"
        :unique-opened="true"
        :router="true"
      >
        <!-- 1 一级菜单 -->
        <el-sub-menu
          :index="menu.id + ''"
          v-for="menu in newMenus"
          :key="menu.id"
        >
          <!-- 一级标题+图标 -->
          <template #title>
            <el-icon><icon-menu /></el-icon>
            <span> {{ menu.title }}</span>
          </template>
          <!-- 1-1 二级菜单 -->
          <el-menu-item
            index="1-1"
            v-for="submenu in menu.children"
            key="submenu.id"
            >{{ submenu.title }}</el-menu-item
          >
        </el-sub-menu>

        <!-- <el-menu-item index="2">
          <el-icon><icon-menu /></el-icon>
          <span>Navigator Two</span>
        </el-menu-item>

        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>Navigator Four</span>
        </el-menu-item> -->
      </el-menu>
    </div>
    <div class="homepage_content">
      
      
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, reactive, toRefs, ref } from "vue";
import { useStore } from "vuex";
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from "@element-plus/icons-vue";
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
/*
  如果传到前端的是数组那么要获取数据则要进行很多次遍历，而且非常麻烦
  所以我们采取使用对象的方式来进行，也就是找出key:value 的对应关系
  {:}
*/
// 定义key的接口约束 也就是MenuObj
interface MenuObj {
  parentId: number;
  id: number;
  title: string;
  children?: MenuObj[];
}

// 创建新的菜单的接口，因为没有对id的类型进行约束，所以我们直接写在外面
interface NewMenus {
  [key: number]: MenuObj;
}

const store = useStore();
// 获取数据
const newMenus: NewMenus = store.getters.getNewMenus;
</script>

<style lang="less" scoped>
.homepage_container {
  // position: relative;
  width: ~"@{width}px";
  height: 100%;
  .homepage_header {
    height: 70px;
    width: ~"@{width}px";
    background-color: rgb(9, 125, 240);
  }
  .homepage_menu {
    position: absolute;
    top: 70px;
    left: 0;
    bottom: 0;
    width: 250px;
    background-color: rgb(230, 29, 29);
  }
  .homepage_content {
    position: absolute;
    top: 70px;
    right: 0;
    left: 200px;
    bottom: 0;
    background-color: aquamarine;
  }
}

@width: 1440;
@screen: 1920;

.pxToVW (@px, @max, @attr: width) {
  @vw: (@px / @max) * 100;
  @{attr}: ~"@{vw}vw";
}

.content {
  height: 100%;
  width: ~"@{width}px";
  margin: 0 auto;
  padding-bottom: 18px;
}

@media screen and (max-width: ~"@{screen}px") {
  .first-install .homepage_container {
    .pxToVW(@width, @screen);
  }
}
</style>










