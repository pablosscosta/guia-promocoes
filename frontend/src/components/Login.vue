<template>
  <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)] p-4">
    <h1 class="text-4xl font-bold text-blue-700 mb-6">Login</h1>
    <form @submit.prevent="handleLogin" class="w-full max-w-sm space-y-4">
      <div>
        <label for="username" class="block text-gray-700">Usuário</label>
        <input
          id="username"
          v-model="username"
          type="text"
          required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <div>
        <label for="password" class="block text-gray-700">Senha</label>
        <input
          id="password"
          v-model="password"
          type="password"
          required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <button
        type="submit"
        class="w-full px-4 py-2 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 transition-colors duration-300"
      >
        Entrar
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'

const router = useRouter()

const username = ref('')
const password = ref('')

const handleLogin = async () => {
  try {
    const response = await api.post('/auth/login/', {
      username: username.value,
      password: password.value,
    })

    localStorage.setItem('access_token', response.data.access)
    router.push('/dashboard')
  } catch (error) {
    console.error('Erro no login:', error)
    alert('Usuário ou senha inválidos')
  }
}
</script>
