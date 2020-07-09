<template>
    <div class="login-box">
        <el-form :rules="account" ref="loginForm" :model="loginForm" label-position="right" label-width="auto" show-message>
            <span class="login-title">欢迎登录</span>
            <div style="margin-top: 5px"></div>
            <el-form-item label="用户名" prop="username">
                <el-col :span="22">
                    <el-input type="text" v-model="loginForm.username"></el-input>
                </el-col>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-col :span="22">
                    <el-input type="password" v-model="loginForm.password"></el-input>
                </el-col>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="handleLogin('loginForm')">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    // import { requestLogin } from '../api/api';
    import {Login} from '../requests/api'
    export default {
        name: "Login",
        data() {
            return {
                logining: false,
                loginForm: {
                    username: '',
                    password: ''
                },

                account: {
                    username: [
                        { required: true, message: '请输入账号', trigger: 'blur' },
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'blur' },
                    ]
                },
                checked: true
            };
        },
        methods: {

            handleLogin() {
                this.$refs.loginForm.validate((valid) => {
                    if (valid) {
                        this.logining = true;
                        let loginParams = {
                            username: this.loginForm.username,
                            password: this.loginForm.password
                        };
                        // 调用axios登录接口
                        console.log(loginParams.username)

                        Login.getLogin(loginParams).then(res => {
                            // debugger;
                            let {code, msg, user } = res;
                            if (code === 200) {
                                // elementui中提示组件
                                this.$message({
                                    type: 'success',
                                    message: msg
                                });
                                // 登陆成功，用户信息就保存在sessionStorage中
                                sessionStorage.setItem('user', JSON.stringify(user));
                                // 跳转到后台主页面
                                console.log('this',this);
                                this.$router.push({ path: '/home' })

                            }else {
                                this.$message({
                                    type: 'error',
                                    message: msg,
                                });
                            }
                        }).catch(err =>{
                            console.log(err);
                        });
                    }else {
                        console.log('error submit!');
                        return false;
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .login-box {
        border: 1px solid #DCDFE6;
        width: 350px;
        margin: 180px auto;
        padding: 35px 35px 15px 35px;
        border-radius: 5px;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        box-shadow: 0 0 25px palegreen;
    }
    .login-title {
        text-align: center;
        margin: 0 auto 40px auto;
        color: #66CD00;
        font-size: 30px;
        font-weight: bold;
    }
</style>
