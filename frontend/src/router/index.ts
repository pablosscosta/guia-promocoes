import { createRouter, createWebHistory } from 'vue-router'
import EstablishmentList from '../pages/establishment/EstablishmentList.vue'
import PromotionList from '../pages/promotion/PromotionList.vue'
import Home from '../pages/Home.vue'

const routes= [
    { path: '/', component: Home},
    { path: '/establishments', component: EstablishmentList},
    { path: '/promotions', component: PromotionList}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;