<template>
  <div class="home">
    <el-button type="text" @click="hello">Helloworld</el-button>
    <el-container>
      <el-header>Header</el-header>
      <el-main>Main</el-main>
    </el-container>
    <div id="container"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
export default {

  name: 'Home',
  props: {
    msg: String
  },
  methods:{
    hello: function () {
      var dom = document.getElementById("container");
      var myChart = echarts.init(dom);
      let option = null;

      option = {
        xAxis: {
          type: 'category',
          boundaryGap: false
        },
        yAxis: {
          type: 'value',
          boundaryGap: [0, '30%']
        },
        visualMap: {
          type: 'piecewise',
          show: false,
          dimension: 0,
          seriesIndex: 0,
          pieces: [{
            gt: 1,
            lt: 3,
            color: 'rgba(0, 180, 0, 0.5)'
          }, {
            gt: 5,
            lt: 7,
            color: 'rgba(0, 180, 0, 0.5)'
          }]
        },
        series: [
          {
            type: 'line',
            smooth: 0.6,
            symbol: 'none',
            lineStyle: {
              color: 'green',
              width: 5
            },
            markLine: {
              symbol: ['none', 'none'],
              label: {show: false},
              data: [
                {xAxis: 1},
                {xAxis: 3},
                {xAxis: 5},
                {xAxis: 7}
              ]
            },
            areaStyle: {},
            data: [
              ['2019-10-10', 200],
              ['2019-10-11', 400],
              ['2019-10-12', 650],
              ['2019-10-13', 500],
              ['2019-10-14', 250],
              ['2019-10-15', 300],
              ['2019-10-16', 450],
              ['2019-10-17', 300],
              ['2019-10-18', 100]
            ]
          }
        ]
      };
      if (option && typeof option === "object") {
        myChart.setOption(option, true);
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #container {
    color: #97ffb3;
    height: 600px;
    width: 100%;
    margin: auto;
  }
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
