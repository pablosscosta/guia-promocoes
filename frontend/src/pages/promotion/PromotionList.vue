<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold text-neutral-dark mb-6 text-center">
      Promoções
    </h1>

    <!-- Botão de retornar -->
    <div class="flex justify-center mb-6">
      <router-link
        to="/"
        class="flex items-center gap-2 px-6 py-2 bg-neutral-dark text-white font-semibold rounded-lg shadow-md hover:bg-neutral-dark/80 transition-colors duration-300"
      >
        ⬅️ Retornar
      </router-link>
    </div>

    <!-- Lista de promoções -->
    <section class="bg-white rounded-lg shadow-md p-6 border-t-4 border-primary-600">
      <ul v-if="promotions.length > 0">
        <li v-for="promo in promotions" :key="promo.id" class="p-4 border-b">
          <p class="font-bold">{{ promo.title }}</p>
          <p class="text-sm text-neutral-dark/70">{{ promo.description }}</p>
          <p class="text-sm text-neutral-dark/70">Preço: R$ {{ promo.price }}</p>
        </li>
      </ul>
      <p v-else class="text-neutral-dark/70">Nenhuma promoção encontrada.</p>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import api from "../../services/api";

const promotions = ref<any[]>([]);
const loading = ref(true);
const error = ref<any>(null);

onMounted(async () => {
  try {
    const { data } = await api.get("/promotions/");
    promotions.value = data;
  } catch (err: any) {
    error.value = err;
    console.error("Erro ao carregar promoções:", err);
  } finally {
    loading.value = false;
  }
});
</script>
