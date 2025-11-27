import axios from 'axios'
import router from '../router'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
})

// Interceptor de requisição: adiciona token
api.interceptors.request.use(config => {
  const userData = localStorage.getItem('user')
  if (userData) {
    const user = JSON.parse(userData)
    if (user.token) {
      config.headers.Authorization = `Bearer ${user.token}`
    }
  }
  return config
})

// Interceptor de resposta: trata erros
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // Token inválido ou expirado → remove e redireciona
      localStorage.removeItem('access_token')
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

export default api
