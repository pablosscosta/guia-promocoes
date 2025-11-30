import { createRouter, createWebHistory } from 'vue-router'
import EstablishmentList from '../pages/establishment/EstablishmentList.vue'
import PromotionList from '../pages/promotion/PromotionList.vue'
import Home from '../pages/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import DashboardEstablishment from '../components/dashboard/DashboardEstablishment.vue'
import DashboardClient from '../components/dashboard/DashboardClient.vue'
import { useAuthStore } from '../store/auth'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/establishments', name: 'Establishments', component: EstablishmentList },
  { path: '/promotions', name: 'Promotions', component: PromotionList },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/dashboard/establishment', name: 'DashboardEstablishment', component: DashboardEstablishment },
  { path: '/dashboard/client', name: 'DashboardClient', component: DashboardClient }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to, _from, next) => {
  const auth = useAuthStore()
  await auth.loadUser()

  if (typeof to.name === "string" && to.name.startsWith("Dashboard")) {
    if (!auth.user) {
      next({ name: "Login" })
    } else {
      if (to.name === "DashboardEstablishment" && auth.user.role === "estabelecimento") {
        next()
      } else if (to.name === "DashboardClient" && auth.user.role === "cliente") {
        next()
      } else {
        next({ name: "Login" })
      }
    }
  } else {
    next()
  }
})

export default router
