<template>
  <!-- Container principal da página de dashboard -->
  <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)] p-4">
    
    <!-- Título da página -->
    <h1 class="text-4xl font-bold text-primary-700 mb-6">Dashboard</h1>

    <!-- Mensagem de carregamento -->
    <div v-if="loading" class="text-neutral-dark">Carregando dados...</div>

    <!-- Conteúdo principal -->
    <div v-else>
      <!-- Saudação ao usuário -->
      <p class="text-xl text-neutral-dark mb-4">
        Bem-vindo, <span class="font-semibold">{{ user?.username }}</span>!
      </p>

      <!-- Cards de estatísticas -->
      <div class="grid grid-cols-2 gap-6">
        
        <!-- Card de estabelecimentos -->
        <div class="p-6 bg-primary-100 rounded-lg shadow">
          <h2 class="text-lg font-bold text-primary-700">Estabelecimentos</h2>
          <p class="text-2xl font-extrabold">{{ user?.establishments_count }}</p>
        </div>

        <!-- Card de promoções -->
        <div class="p-6 bg-success-100 rounded-lg shadow">
          <h2 class="text-lg font-bold text-success-700">Promoções</h2>
          <p class="text-2xl font-extrabold">{{ user?.promotions_count }}</p>
        </div>
      </div>

      <!-- Botão de logout -->
      <button
        @click="handleLogout"
        class="mt-8 px-6 py-3 bg-error-600 text-white font-semibold rounded-lg shadow-md hover:bg-error-700 transition-colors duration-300"
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
