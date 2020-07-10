
<template>
  <div id="login">
    <el-form class="info" ref="AccountForm" :model="account" :rules="loginRules">
      <div class="title">LOGIN</div>
      <div class="main">
        <div class="row">
          <p>Login with your account</p>
        </div>
        <el-form-item prop="username">
          <el-input
            placeholder="User Name"
            prefix-icon="el-icon-s-custom"
            v-model="account.username"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            placeholder="password"
            prefix-icon="el-icon-lock"
            v-model="account.password"
            show-password
          ></el-input>
        </el-form-item>
        <div class="row">
          <el-checkbox v-model="checked">Remember Me</el-checkbox>
          <a href="#">Forget password</a>
        </div>
        <el-form-item>
          <el-button @click="handleSubmit">Login</el-button>
        </el-form-item>
        <div class="row">
          <p>
            if you do not have an account,
            <a href="#">Sign up</a>
          </p>
        </div>
      </div>
    </el-form>
  </div>
</template>
<script>
import { Login } from "../axios/api";
export default {
  name: "Login",
  data() {
    return {
      account: {
        username: "",
        password: ""
      },

      loginRules: {
        username: [{ required: true, message: "请输入账号", trigger: "blur" }],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }]
      },
      checked: true,
    };
  },
  methods: {
    handleSubmit(ev) {
      this.$refs.AccountForm.validate(valid => {
        if (valid) {
          this.logining = true;
          let loginParams = {
            username: this.account.username,
            password: this.account.password
          };
          // 调用axios登录接口
          Login.requseLogin(loginParams)
            .then(res => {
              // 根据返回的code判断是否成功
              let { code, msg, user } = res;
              if (code === 200) {
                // elementui中提示组件
                this.$message({
                  type: "success",
                  message: msg
                });
                // 登陆成功，用户信息就保存在sessionStorage中
                sessionStorage.setItem("user", JSON.stringify(user));
                // 跳转到后台主页面
                console.log("this", this);
                this.$router.push({ path: "/Home" });
              } else {
                this.$message({
                  type: "error",
                  message: msg
                });
              }
            })
            .catch(err => {
              console.log(err);
            });
        } else {
          console.log("error submit!");
          return false;
        }
      });
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped >
@import "../assets/style/Login.css";
</style> 