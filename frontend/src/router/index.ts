import { createRouter, createWebHistory } from 'vue-router'
import EstablishmentList from '../pages/establishment/EstablishmentList.vue'
import PromotionList from '../pages/promotion/PromotionList.vue'
import Home from '../pages/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import DashboardEstablishment from '../components/dashboard/DashboardEstablishment.vue'
import DashboardClient from '../components/dashboard/DashboardClient.vue'
import { useAuthStore } from '../store/auth'

const routes= [
    { path: '/', component: Home},
    { path: '/establishments', component: EstablishmentList},
    { path: '/promotions', component: PromotionList},
    { path: '/login', component: Login},
    { path: '/register', component: Register},
    { path: '/dashboard/establishment', component: DashboardEstablishment},
    { path: '/dashboard/client', component: DashboardClient}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, _from, next) => {
  const auth = useAuthStore()
  auth.loadUser()

  if (to.path.startsWith('/dashboard')) {
    if (!auth.user) {
      next('/login')
    } else {
      if (to.path === '/dashboard/establishment' && auth.user.role === 'estabelecimento') {
        next()
      } else if (to.path === '/dashboard/client' && auth.user.role === 'cliente') {
        next()
      } else {
        next('/login')
      }
    }
  } else {
    next()
  }
})


export default router;