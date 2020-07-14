<template>
  <div id="headbar">
    <img id="logo" src="../../assets/images/ICBC_logo.jpg">
  </div>
</template>
<script>
export default {
  name: "headbar",
  data() {
    return {};
  }
};
</script>
<style scoped>
#headbar{
    height: 50px;
    background-color: #fff;
    margin-bottom: 50px;
    border-bottom: 1px solid #ccc;
}
#logo {
    height: 50px;
}
</style>