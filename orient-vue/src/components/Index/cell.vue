<template>
<div class="cell">
    <img class="icon" src="../../assets/images/cell_icon.png">
    <div class="main">
      <p>Total Profit</p>
      <span>1,012</span>
    </div>
</div>
</template>
<script>
export default {
  name: "cell",
  data() {
    return {
    };
  }
};
</script>
<style scoped>
.cell{
    flex: 1 1 20%;
    height: 90%;
    background-color: white;
    margin: 5px 20px;
    display: flex;
    align-items: center;
    /* border: 1px solid green; */
    box-shadow: 5px 5px 10px #ddd,
    -5px 5px 10px #ddd,
    5px -5px 10px #ddd,
    -5px -5px 10px #ddd;
}
.icon{
  width: 40px;
  height: 40px;
  /* border: 1px solid blue; */
  margin:0 30px;
}
.main>p{
  color: #aaa;
  height: 30px;
  line-height: 30px;
  font-size: 14px;
}
.main>span{
  font-weight: bold;
  font-size: 18px;
}
</style>