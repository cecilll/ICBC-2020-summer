import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:80';

export const Login = {
    async getLogin(params){
        console.log(params);
        let res = await axios.post('/user/login', params);
        res = res.data;
        return res
    }
};
