import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index.ts'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'

createApp(App).use(router).mount('#app')
