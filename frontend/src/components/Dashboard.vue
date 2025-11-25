<template>
  <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)] p-4">
    <h1 class="text-4xl font-bold text-blue-700 mb-6">Dashboard</h1>

    <div v-if="loading" class="text-gray-600">Carregando dados...</div>

    <div v-else>
      <p class="text-xl text-gray-700 mb-4">
        Bem-vindo, <span class="font-semibold">{{ user?.username }}</span>!
      </p>

      <div class="grid grid-cols-2 gap-6">
        <div class="p-6 bg-blue-100 rounded-lg shadow">
          <h2 class="text-lg font-bold text-blue-700">Estabelecimentos</h2>
          <p class="text-2xl font-extrabold">{{ user?.establishments_count }}</p>
        </div>

        <div class="p-6 bg-green-100 rounded-lg shadow">
          <h2 class="text-lg font-bold text-green-700">Promoções</h2>
          <p class="text-2xl font-extrabold">{{ user?.promotions_count }}</p>
        </div>
      </div>

      <button
        @click="handleLogout"
        class="mt-8 px-6 py-3 bg-red-600 text-white font-semibold rounded-lg shadow-md hover:bg-red-700 transition-colors duration-300"
      >
        Logout
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'

const router = useRouter()
const user = ref<any>(null)
const loading = ref(true)

onMounted(async () => {
  try {
    const response = await api.get('/auth/me/')
    user.value = response.data
  } catch (error) {
    console.error('Erro ao carregar dados do usuário:', error)
    router.push('/login')
  } finally {
    loading.value = false
  }
})

const handleLogout = () => {
  localStorage.removeItem('access_token')
  router.push('/')
}
</script>
