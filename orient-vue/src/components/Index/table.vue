 <template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="date" label="日期" width="180"></el-table-column>
    <el-table-column prop="name" label="姓名" width="180"></el-table-column>
    <el-table-column prop="address" label="地址"></el-table-column>
  </el-table>
</template>

  <script>
export default {
  data() {
    return {
      tableData: [
        {
          date: "2020-07-14",
          name: "王瑞璞",
          address: "湖北省武汉市樱花大厦"
        }
      ]
    };
  }
};
</script>