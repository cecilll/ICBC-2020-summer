import $axios from "./server.util";

const Login = data => {
    return $axios({
        url: '/Login',
        method: 'get',
        data
    })
};

// export const Login = {
//     async getLogin(params){
//         console.log(params);
//         let res = await axios.post('/user/login', params);
//         res = res.data;
//         return res
//     }
// };

export default {
    Login
}