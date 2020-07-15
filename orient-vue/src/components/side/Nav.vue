<template>
  <div id="navbar">
    <el-menu
      default-active="2"
      @open="handleOpen"
      @close="handleClose"
      background-color="#204051"
      text-color="#e5e5e5"
      active-text-color="#ea9a96"
    >
      <div class="title">
        <span>组合资产投资分析</span>
      </div>
      
      <el-menu-item index="1">
        <i class="el-icon-pie-chart"></i>
        <span slot="title">评估分析</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-user-solid"></i>
        <span slot="title">个人中心</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "navbar",
  data() {
    return {};
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>
<style scoped>
#navbar {
  height: 100%;
  width: 200px;
}
.el-menu {
  height: 100%;
}
.title{
  text-align: center;
  color: #fff;
  height: 50px;
  line-height: 50px;
  border-bottom: 1px solid rgb(220,222,226);
  font-size: 14px;
}
</style>