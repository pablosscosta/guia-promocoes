<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Nossos Estabelecimentos Parceiros</h1>

    <div class="flex justify-center mb-6 space-x-4">
      <button @click="showModal = true"
              class="px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 transition-colors duration-300">
        Cadastrar Estabelecimento
      </button>
      <router-link to="/"
                   class="px-6 py-2 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition-colors duration-300">
        Retornar
      </router-link>
    </div>

    <EstablishmentModal v-if="showModal"
                        @close="showModal = false"
                        @saved="onEstablishmentSaved" />

    <p v-if="loading" class="text-center text-lg text-blue-600">Carregando estabelecimentos...</p>
    <p v-else-if="error" class="text-center text-lg text-red-600">Erro ao carregar estabelecimentos: {{ error.message }}</p>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="establishment in establishments" :key="establishment.id"
           class="bg-white rounded-lg shadow-md p-6 border-t-4 border-blue-500 hover:shadow-lg transition-shadow duration-300">
        <h2 class="text-xl font-semibold text-gray-900 mb-2">{{ establishment.name }}</h2>
        <p class="text-gray-600 mb-1"> {{ establishment.phone_number }}</p>
        <p class="text-gray-600 mb-3"> {{ establishment.address }}</p>
        <div class="flex flex-wrap gap-2">
          <span v-for="category in establishment.categories" :key="category.id"
                class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full">
            {{ category.name }}
          </span>
        </div>
      </div>
    </div>

    <p v-if="!loading && !error && establishments.length === 0" class="text-center text-lg text-gray-500 mt-8">
      Nenhum estabelecimento encontrado.
    </p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import EstablishmentModal from '../../components/EstablishmentModal.vue'

const establishments = ref([]);
const loading = ref(true);
const error = ref(null)
const showModal = ref(false)

onMounted(async () => {
  try {
    const response = await axios.get('establishments/');
    establishments.value = response.data;
  } catch (error) {
    error.value = error;
    console.error("Erro ao buscar estabelecimentos:", error);
  } finally {
    loading.value = false;
  }
});

function onEstablishmentSaved() {
  loading.value = true;
  axios.get('establishments/')
    .then(res => establishments.value = res.data)
    .catch(err => error.value = err)
    .finally(() => loading.value = false);
}

</script>