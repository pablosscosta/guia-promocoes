<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">
      Nossas Promoções
    </h1>

    <div class="flex justify-center mb-6 space-x-6">
      <button @click="showModal = true"
              class="px-6 py-2 bg-green-600 text-white font-semibold rounded-lg shadow-md hover:bg-green-700 transition-colors duration-300">
        Cadastrar Promoção
      </button>

      <router-link to="/"
                   class="px-6 py-2 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition-colors duration-300">
        Retornar
      </router-link>
    </div>

    <PromotionModal v-if="showModal"
                    @close="showModal = false"
                    @saved="onPromotionSaved" />

    <p v-if="loading" class="text-center text-lg text-blue-600">Carregando promoções...</p>
    <p v-else-if="error" class="text-center text-lg text-red-600">Erro ao carregar promoções: {{ error.message }}</p>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="promotion in promotions" :key="promotion.id"
           class="bg-white rounded-lg shadow-md p-6 border-t-4 border-blue-500 hover:shadow-lg transition-shadow duration-300">
        <h2 class="text-xl font-semibold text-gray-900 mb-2">{{ promotion.title }}</h2>
        <p class="text-gray-600 mb-1"> {{ promotion.description }}</p>
        <p class="text-gray-800 mb-3">Estabelecimento: {{ promotion.establishment_name }}</p>
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
import PromotionModal from '../../components/PromotionModal.vue'

const promotions = ref([]);
const loading = ref(true);
const error = ref(null)
const showModal = ref(false)

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
function onPromotionSaved() {
  loading.value = true;
  axios.get('promotions/')
    .then(res => promotions.value = res.data)
    .catch(err => error.value = err)
    .finally(() => loading.value = false);
}
</script>