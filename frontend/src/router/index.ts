import { createRouter, createWebHistory } from 'vue-router'
import EstablishmentList from '../pages/establishment/EstablishmentList.vue'
import PromotionList from '../pages/promotion/PromotionList.vue'
import Home from '../pages/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Dashboard from '../components/Dashboard.vue'

const routes= [
    { path: '/', component: Home},
    { path: '/establishments', component: EstablishmentList},
    { path: '/promotions', component: PromotionList},
    { path: '/login', component: Login},
    { path: '/register', component: Register},
    { path: '/dashboard', component: Dashboard}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;