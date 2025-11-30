<template>
  <!-- Container principal da página de login -->
  <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)] p-4 bg-gradient-to-br from-neutral-light via-white to-primary-50">
    
    <!-- Card central -->
    <div class="w-full max-w-sm bg-white/90 rounded-lg shadow-lg p-8">
      
      <!-- Título da página -->
      <h1 class="text-3xl font-bold text-primary-700 mb-6 text-center">Login</h1>
      
      <!-- Formulário de login -->
      <form @submit.prevent="login" class="space-y-4">
        
        <!-- Campo usuário -->
        <div>
          <label for="username" class="block text-neutral-dark font-medium mb-1">Usuário</label>
          <input
            id="username"
            v-model="username"
            type="text"
            required
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-600"
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
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-600"
          />
        </div>

        <!-- Botão de envio -->
        <button
          type="submit"
          class="w-full px-4 py-2 bg-primary-600 text-white font-semibold rounded-lg shadow-md hover:bg-primary-700 transition-colors duration-300"
        >
          Entrar
        </button>
      </form>

      <!-- Botão para retornar -->
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
import { ref } from "vue";
import api from "../services/api";
import { useAuthStore } from "../store/auth";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const error = ref("");
const router = useRouter();
const auth = useAuthStore();

async function login() {
  try {
    const { data } = await api.post("/auth/login/", {
      username: username.value,
      password: password.value,
    });

    // salvar token
    localStorage.setItem("token", data.access);

    // carregar usuário
    await auth.loadUser();

    // redirecionar conforme role
    if (auth.user && auth.user.role === "estabelecimento") {
      router.push({ name: "DashboardEstablishment" });
    } else if (auth.user && auth.user.role === "cliente") {
      router.push({ name: "DashboardClient" });
    }
  } catch (err: any) {
    error.value = "Credenciais inválidas";
  }
}
</script>
