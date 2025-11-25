<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">
      Nossos Estabelecimentos
    </h1>

    <div class="flex justify-center mb-6 space-x-6">
      <button
        @click="openCreateModal"
        class="px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 transition-colors duration-300"
      >
        Cadastrar Estabelecimento
      </button>

      <router-link
        to="/"
        class="px-6 py-2 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition-colors duration-300"
      >
        Retornar
      </router-link>
    </div>

    <!-- Modal -->
    <EstablishmentModal
      v-if="showModal"
      :establishment="selectedEstablishment"
      @close="showModal = false"
      @saved="onEstablishmentSaved"
    />

    <p v-if="loading" class="text-center text-lg text-blue-600">
      Carregando estabelecimentos...
    </p>
    <p v-else-if="error" class="text-center text-lg text-red-600">
      Erro ao carregar estabelecimentos: {{ error.message }}
    </p>

    <!-- Lista + barra de busca e filtro -->
    <div v-else>
      <!-- Barra de busca e filtro -->
      <div class="flex justify-center mb-6 space-x-6">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Buscar estabelecimento..."
          class="px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <select
          v-model="selectedCategory"
          class="px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="">Todas categorias</option>
          <option
            v-for="cat in uniqueCategories"
            :key="cat"
            :value="cat"
          >
            {{ cat }}
          </option>
        </select>
      </div>

      <!-- Lista filtrada -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="establishment in filteredEstablishments"
          :key="establishment.id"
          class="bg-white rounded-lg shadow-md p-6 border-t-4 border-blue-500 hover:shadow-lg transition-shadow duration-300"
        >
          <h2 class="text-xl font-semibold text-gray-900 mb-2">
            {{ establishment.name }}
          </h2>
          <p class="text-gray-600 mb-1">{{ establishment.address }}</p>
          <div class="flex flex-wrap gap-2 mb-3">
            <span v-for="c in establishment.categories" :key="c.id" class="px-2 py-1 bg-gray-200 text-gray-800 rounded-md text-sm">
              {{ c.name }}
            </span>
          </div>

          <!-- Botão Editar -->
          <button
            @click="editEstablishment(establishment)"
            class="px-3 py-1 bg-yellow-500 text-white rounded hover:bg-yellow-600"
          >
            Editar
          </button>
          <!-- Botão Excluir -->
          <button
            @click="deleteEstablishment(establishment.id)"
            class="ml-2 px-3 py-1 bg-red-600 text-white rounded hover:bg-red-700"
          >
            Excluir
          </button>
        </div>
      </div>

      <p
        v-if="!loading && !error && filteredEstablishments.length === 0"
        class="text-center text-lg text-gray-500 mt-8"
      >
        Nenhum estabelecimento encontrado.
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import api from '../../services/api';
import { ref, onMounted, computed } from 'vue';
import EstablishmentModal from '../../components/EstablishmentModal.vue';

const establishments = ref([]);
const loading = ref(true);
const error = ref(null);
const showModal = ref(false);
const selectedEstablishment = ref(null);
const searchTerm = ref("");
const selectedCategory = ref("");

const uniqueCategories = computed(() => {
  const set = new Set();
  establishments.value.forEach(e => {
    if (e.categories) {
      e.categories.forEach(c => set.add(c.name));
    }
  });
  return Array.from(set).sort();
});

const filteredEstablishments = computed(() => {
  return establishments.value.filter(e => {
    const term = searchTerm.value.trim().toLowerCase();
    const matchesSearch =
      !term || (e.name && e.name.toLowerCase().includes(term));

    const matchesCategory =
      !selectedCategory.value ||
      (e.categories && e.categories.some(c => c.name === selectedCategory.value));

    return matchesSearch && matchesCategory;
  });
});

onMounted(async () => {
  try {
    const response = await api.get('establishments/');
    establishments.value = response.data;
  } catch (err) {
    error.value = err;
    console.error("Erro ao buscar estabelecimentos:", err);
  } finally {
    loading.value = false;
  }
});

function onEstablishmentSaved() {
  loading.value = true;
  api.get('establishments/')
    .then(res => establishments.value = res.data)
    .catch(err => {
      error.value = err;
      console.error("Erro ao atualizar estabelecimentos:", err);
    })
    .finally(() => loading.value = false);
}

function openCreateModal() {
  selectedEstablishment.value = null;
  showModal.value = true;
}

function editEstablishment(est: any) {
  selectedEstablishment.value = est;
  showModal.value = true;
}

async function deleteEstablishment(id: number) {
  if (!confirm("Tem certeza que deseja excluir este estabelecimento?")) return;
  try {
    await api.delete(`establishments/${id}/`);
    establishments.value = establishments.value.filter(e => e.id !== id);
  } catch (err) {
    console.error("Erro ao excluir estabelecimento:", err);
    alert("Erro ao excluir estabelecimento.");
  }
}
</script>
