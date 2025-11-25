<template>
  <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)] p-4">
    <h1 class="text-4xl font-bold text-purple-700 mb-6">Cadastro</h1>
    <form @submit.prevent="handleRegister" class="w-full max-w-sm space-y-4">
      <div>
        <label for="username" class="block text-gray-700">Usuário</label>
        <input
          id="username"
          v-model="username"
          type="text"
          required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
        />
      </div>

      <div>
        <label for="password" class="block text-gray-700">Senha</label>
        <input
          id="password"
          v-model="password"
          type="password"
          required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
        />
      </div>

      <button
        type="submit"
        class="w-full px-4 py-2 bg-purple-600 text-white font-semibold rounded-lg shadow-md hover:bg-purple-700 transition-colors duration-300"
      >
        Cadastrar
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

const handleRegister = async () => {
  try {
    await api.post('/auth/register/', {
      username: username.value,
      password: password.value,
    })
    alert('Cadastro realizado com sucesso!')
    router.push('/login')
  } catch (error) {
    console.error('Erro no cadastro:', error)
    alert('Não foi possível realizar o cadastro')
  }
}
</script>
