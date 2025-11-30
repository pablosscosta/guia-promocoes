import { defineStore } from 'pinia'
import api from '../services/api'

type User = {
  username: string
  role: 'cliente' | 'estabelecimento'
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as User | null
  }),
  actions: {
    async loadUser() {
      const token = localStorage.getItem("token");
      if (!token) {
        this.user = null;
        return;
      }
      try {
        const { data } = await api.get("/auth/me/details/");
        this.user = data;
      } catch (err) {
        this.user = null;
        localStorage.removeItem("token");
      }
    }
  }
})
