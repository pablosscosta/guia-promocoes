import { defineStore } from 'pinia'

type User = {
  username: string
  role: 'cliente' | 'estabelecimento'
  token?: string
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as User | null
  }),
  actions: {
    setUser(userData: User) {
      this.user = userData
      localStorage.setItem('user', JSON.stringify(userData))
    },
    loadUser() {
      const data = localStorage.getItem('user')
      if (data) this.user = JSON.parse(data) as User
    },
    logout() {
      this.user = null
      localStorage.removeItem('user')
    }
  }
})