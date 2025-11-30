<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold text-neutral-dark mb-6 text-center">
      Dashboard do Cliente
    </h1>

    <!-- Perfil -->
    <section class="bg-white rounded-lg shadow-md p-6 border-t-4 border-primary-600">
      <h2 class="text-xl font-semibold mb-4">Meu Perfil</h2>
      <p class="text-neutral-dark/70">Usuário: {{ user?.username }}</p>
      <p class="text-neutral-dark/70">Email: {{ user?.email }}</p>
      <p class="text-neutral-dark/70">Perfil: {{ user?.role }}</p>
      <button @click="logout" class="btn btn-danger mt-4">Logout</button>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import api from "../../services/api";

const user = ref<any>(null);
const loading = ref(true);
const error = ref<any>(null);

onMounted(async () => {
  try {
    const { data: me } = await api.get("/auth/me/details/");
    user.value = {
      id: me.id,
      username: me.username,
      email: me.email,
      role: me.role,
    };
  } catch (err: any) {
    error.value = err;
    console.error("Erro ao carregar detalhes:", err);
  } finally {
    loading.value = false;
  }
});

function logout() {
  // limpar token e redirecionar para login
  localStorage.removeItem("token");
  window.location.href = "/login";
}
</script>
