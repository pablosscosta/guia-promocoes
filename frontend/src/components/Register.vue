<template>
  <!-- Container principal da página de cadastro -->
  <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)] p-4 bg-gradient-to-br from-neutral-light via-white to-primary-50">
    
    <!-- Card central -->
    <div class="w-full max-w-sm bg-white/90 rounded-lg shadow-lg p-8">
      
      <!-- Título da página -->
      <h1 class="text-3xl font-bold text-secondary-700 mb-6 text-center">Cadastro</h1>
      
      <!-- Formulário de cadastro -->
      <form @submit.prevent="handleRegister" class="space-y-4">
        
        <!-- Campo usuário -->
        <div>
          <label for="username" class="block text-neutral-dark font-medium mb-1">Usuário</label>
          <input
            id="username"
            v-model="username"
            type="text"
            required
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-secondary-600"
          />
        </div>

        <!-- Campo senha -->
        <div>
          <label for="password" class="block text-neutral-dark font-medium mb-1">Senha</label>
          <input
            id="password"
            v-model="password"
            type="password"
            required
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-secondary-600"
          />
        </div>

        <!-- Botão de envio -->
        <button
          type="submit"
          class="w-full px-4 py-2 bg-secondary-600 text-white font-semibold rounded-lg shadow-md hover:bg-secondary-700 transition-colors duration-300"
        >
          Cadastrar
        </button>
      </form>

      <!-- Botão de retornar -->
      <div class="mt-6 flex flex-col justify-center items-center gap-4">
        <router-link
          to="/"
          class="inline-flex items-center gap-1 px-3 py-1 bg-neutral-dark text-white rounded hover:bg-neutral-dark/80 transition-colors"
        >
          ⬅️ Retornar
        </router-link>
      </div>
    </div>
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
