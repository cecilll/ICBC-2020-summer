import axios from 'axios'
axios.defaults.baseURL = "127.0.0.1:80"
export const Login = {
    async requseLogin(params) {
        let res = await axios.post('user/login', params)
        res = res.data;
        return res
    }
} 