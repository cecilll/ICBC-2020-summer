import Vue from 'vue'
import Router from 'vue-router'
import Home from "@/components/Home"
import Login from "@/components/Login"
import index from "@/components/Index"


Vue.use(Router);

const router = new Router({
    routes: [{
        path: '/login',
        name: 'login',
        component: Login
    },
        {
            path: '/',
            name: 'home',
            redirect: '/index',
            component: Home,
            children: [
                //首页
                {
                    path: '/index',
                    name: 'index',
                    component: index
                }
            ]
        }
    ]});
router.beforeEach((to, from, next) => {
    let token = sessionStorage.getItem('token');
    if (to.path === '/login') {
        next()
    } else {
        if (token === '' || token == null) {
            next('/login');
        } else {
            next()
        }
    }

});
export default router