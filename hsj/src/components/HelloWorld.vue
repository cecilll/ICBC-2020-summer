<template>
  <div class="hello">
    <el-button type="text" @click="hello">helloworld</el-button>
    helloworld
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods: {
    hello: function () {
      console.log("lhr")
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
