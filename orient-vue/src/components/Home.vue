<template>
  <div id="home">
    <div id="left"><Nav ></Nav></div>
    <div id="right">
      <Header></Header>
      <transition  name="fade" mode="out-in">
        <router-view></router-view>
      </transition>
        <div id="chart" style="height: 800px"></div>
        <div id="pieChart" style="height: 100%"></div>
    </div>
  </div>
</template>

<script>
import echarts from "echarts";
import Header from "./side/Header";
import Nav from "./side/Nav";
export default {
  name: "Home",
  props: {
    msg: String
  },
  components:{
    Nav,
    Header,
    
  },
  mounted(){
    this.creatChart();
    this.pieChart();
  },
  methods: {
    creatChart: function(){
      var dom = document.getElementById("chart");
      var myChart = echarts.init(dom);
      var app = {};
      var option = null;
      var posList = [
        'left', 'right', 'top', 'bottom',
        'inside',
        'insideTop', 'insideLeft', 'insideRight', 'insideBottom',
        'insideTopLeft', 'insideTopRight', 'insideBottomLeft', 'insideBottomRight'
      ];

      app.configParameters = {
        rotate: {
          min: -90,
          max: 90
        },
        align: {
          options: {
            left: 'left',
            center: 'center',
            right: 'right'
          }
        },
        verticalAlign: {
          options: {
            top: 'top',
            middle: 'middle',
            bottom: 'bottom'
          }
        },
        position: {
          options: echarts.util.reduce(posList, function (map, pos) {
            map[pos] = pos;
            return map;
          }, {})
        },
        distance: {
          min: 0,
          max: 100
        }
      };

      app.config = {
        rotate: 90,
        align: 'left',
        verticalAlign: 'middle',
        position: 'insideBottom',
        distance: 15,
        onChange: function () {
          var labelOption = {
            normal: {
              rotate: app.config.rotate,
              align: app.config.align,
              verticalAlign: app.config.verticalAlign,
              position: app.config.position,
              distance: app.config.distance
            }
          };
          myChart.setOption({
            series: [{
              label: labelOption
            }, {
              label: labelOption
            }, {
              label: labelOption
            }, {
              label: labelOption
            }]
          });
        }
      };


      var labelOption = {
        show: true,
        position: app.config.position,
        distance: app.config.distance,
        align: app.config.align,
        verticalAlign: app.config.verticalAlign,
        rotate: app.config.rotate,
        formatter: '{c}  {name|{a}}',
        fontSize: 16,
        rich: {
          name: {
            textBorderColor: '#fff'
          }
        }
      };

      option = {
        color: ['#003366', '#006699', '#4cabce', '#e5323e'],
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        title: {
          text: '近期重仓股展示',
          right: 'center',
        },
        legend: {
          bottom: 'left',
          data: ['Forest', 'Steppe', 'Desert', 'Wetland']
        },
        toolbox: {
          show: true,
          orient: 'vertical',
          left: 'right',
          top: 'center',
          feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
          }
        },
        xAxis: [
          {
            type: 'category',
            axisTick: {show: false},
            data: ['2012', '2013', '2014', '2015', '2016']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Forest',
            type: 'bar',
            barGap: 0,
            label: labelOption,
            data: [320, 332, 301, 334, 390]
          },
          {
            name: 'Steppe',
            type: 'bar',
            label: labelOption,
            data: [220, 182, 191, 234, 290]
          },
          {
            name: 'Desert',
            type: 'bar',
            label: labelOption,
            data: [150, 232, 201, 154, 190]
          },
          {
            name: 'Wetland',
            type: 'bar',
            label: labelOption,
            data: [98, 77, 101, 99, 40]
          }
        ]
      };
      if (option && typeof option === "object") {
        myChart.setOption(option, true);
      }
    },
    pieChart: function () {
      var dom = document.getElementById("pieChart");
      var myChart = echarts.init(dom);
      // var app = {};
      var option = null;
      var weatherIcons = {
        Sunny: '晴朗',
        Cloudy: '多云',
        Showers: '有雨'
      };

      option = {
        title: {
          text: '天气情况统计',
          subtext: '虚构数据',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          // orient: 'vertical',
          // top: 'middle',
          bottom: 10,
          left: 'center',
          data: ['西凉', '益州', '兖州', '荆州', '幽州']
        },
        series: [
          {
            type: 'pie',
            radius: '65%',
            center: ['50%', '50%'],
            selectedMode: 'single',
            data: [
              {
                value: 1548,
                name: '幽州',
                label: {
                  formatter: [
                    '{title|{b}}{abg|}',
                    '  {weatherHead|天气}{valueHead|天数}{rateHead|占比}',
                    '{hr|}',
                    '  {Sunny|}{value|202}{rate|55.3%}',
                    '  {Cloudy|}{value|142}{rate|38.9%}',
                    '  {Showers|}{value|21}{rate|5.8%}'
                  ].join('\n'),
                  backgroundColor: '#eee',
                  borderColor: '#777',
                  borderWidth: 1,
                  borderRadius: 4,
                  rich: {
                    title: {
                      color: '#eee',
                      align: 'center'
                    },
                    abg: {
                      backgroundColor: '#333',
                      width: '100%',
                      align: 'right',
                      height: 25,
                      borderRadius: [4, 4, 0, 0]
                    },
                    Sunny: {
                      height: 30,
                      align: 'left',
                      backgroundColor: {
                        image: weatherIcons.Sunny
                      }
                    },
                    Cloudy: {
                      height: 30,
                      align: 'left',
                      backgroundColor: {
                        image: weatherIcons.Cloudy
                      }
                    },
                    Showers: {
                      height: 30,
                      align: 'left',
                      backgroundColor: {
                        image: weatherIcons.Showers
                      }
                    },
                    weatherHead: {
                      color: '#333',
                      height: 24,
                      align: 'left'
                    },
                    hr: {
                      borderColor: '#777',
                      width: '100%',
                      borderWidth: 0.5,
                      height: 0
                    },
                    value: {
                      width: 20,
                      padding: [0, 20, 0, 30],
                      align: 'left'
                    },
                    valueHead: {
                      color: '#333',
                      width: 20,
                      padding: [0, 20, 0, 30],
                      align: 'center'
                    },
                    rate: {
                      width: 40,
                      align: 'right',
                      padding: [0, 10, 0, 0]
                    },
                    rateHead: {
                      color: '#333',
                      width: 40,
                      align: 'center',
                      padding: [0, 10, 0, 0]
                    }
                  }
                }
              },
              {value: 535, name: '荆州'},
              {value: 510, name: '兖州'},
              {value: 634, name: '益州'},
              {value: 735, name: '西凉'}
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
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
@import "../assets/style/home.css";
</style>
