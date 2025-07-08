<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Promoções</h1>

    <p v-if="loading" class="text-center text-lg text-blue-600">Carregando promoções...</p>
    <p v-else-if="error" class="text-center text-lg text-red-600">Erro ao carregar promoções: {{ error.message }}</p>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="promotion in promotions" :key="promotion.id"
           class="bg-white rounded-lg shadow-md p-6 border-t-4 border-blue-500 hover:shadow-lg transition-shadow duration-300">
        <h2 class="text-xl font-semibold text-gray-900 mb-2">{{ promotion.title }}</h2>
        <p class="text-gray-600 mb-1"> {{ promotion.description }}</p>
        <p class="text-gray-800 mb-3">Estabelecimento: {{ promotion.establishment }}</p>
      </div>
    </div>

    <p v-if="!loading && !error && promotions.length === 0" class="text-center text-lg text-gray-500 mt-8">
      Nenhuma promoção encontrada.
    </p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

const promotions = ref([]);
const loading = ref(true);
const error = ref(null)

onMounted(async () => {
  try {
    const response = await axios.get('promotions/');
    promotions.value = response.data;
  } catch (error) {
    error.value = error;
    console.error("Erro ao buscar promoções:", error);
  } finally {
    loading.value = false;
  }
});
</script>