import Vue from 'vue'
import Router from 'vue-router'
import Home from "@/components/Home"
import Login from "@/components/Login"
import index from "@/components/Index"


Vue.use(Router);

const router = new Router({
    routes: [{
            path: '/',
            name: 'login',
            component: Login
        },
        {
            path: '/home',
            name: 'home',
            redirect: '/index',
            meta: {
                needLogin: true,
            },
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
    ]
});
router.beforeEach((to, from, next) => {
    let token = localStorage.getItem('token');
    if (to.path === '/') {
        next()
    } else {
        if (token === '' || token == null) {
            next('/');
        } else {
            next()
        }
    }

});
export default router