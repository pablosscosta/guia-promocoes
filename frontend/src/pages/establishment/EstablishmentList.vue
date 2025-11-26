<template>
  <div class="container mx-auto p-4">
    
    <!-- Título principal -->
    <h1 class="text-3xl font-bold text-neutral-dark mb-6 text-center">
      Nossos Estabelecimentos
    </h1>

    <!-- Ações principais -->
    <div class="flex justify-center mb-6 space-x-6">
      <!-- Botão cadastrar -->
      <button
        @click="openCreateModal"
        class="px-6 py-2 bg-primary-600 text-white font-semibold rounded-lg shadow-md hover:bg-primary-700 transition-colors duration-300"
      >
        Cadastrar Estabelecimento
      </button>

      <!-- Botão retornar -->
      <router-link
        to="/"
        class="flex items-center gap-2 px-6 py-2 bg-neutral-dark text-white font-semibold rounded-lg shadow-md hover:bg-neutral-dark/80 transition-colors duration-300"
      >
        ⬅️ Retornar
      </router-link>
    </div>

    <!-- Modal -->
    <EstablishmentModal
      v-if="showModal"
      :establishment="selectedEstablishment"
      @close="showModal = false"
      @saved="onEstablishmentSaved"
    />

    <!-- Mensagens de estado -->
    <p v-if="loading" class="text-center text-lg text-primary-600">
      Carregando estabelecimentos...
    </p>
    <p v-else-if="error" class="text-center text-lg text-error-600">
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
          class="w-full md:w-1/3 px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-600"
        />

        <select
          v-model="selectedCategory"
          class="px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-600"
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
          class="bg-white rounded-lg shadow-md p-6 border-t-4 border-primary-600 hover:shadow-lg transition-shadow duration-300"
        >
          <!-- Nome -->
          <h2 class="text-xl font-semibold text-neutral-dark mb-2">
            {{ establishment.name }}
          </h2>
          <!-- Endereço -->
          <p class="text-neutral-dark/70 mb-1">{{ establishment.address }}</p>
          
          <!-- Categorias -->
          <div class="flex flex-wrap gap-2 mb-3">
            <span v-for="c in establishment.categories" :key="c.id"
                  class="px-2 py-1 bg-neutral-light text-neutral-dark rounded-md text-sm">
              {{ c.name }}
            </span>
          </div>

          <!-- Botão Editar -->
          <button
            @click="editEstablishment(establishment)"
            class="px-3 py-1 bg-primary-600 text-white rounded hover:bg-warning-600"
          >
            ✏️ Editar
          </button>
          <!-- Botão Excluir -->
          <button
            @click="deleteEstablishment(establishment.id)"
            class="ml-2 px-3 py-1 bg-secondary-600 text-white rounded hover:bg-error-700"
          >
            🗑️ Excluir
          </button>
        </div>
      </div>

      <!-- Mensagem lista vazia -->
      <p
        v-if="!loading && !error && filteredEstablishments.length === 0"
        class="text-center text-lg text-neutral-dark/60 mt-8"
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
    .then(res => {
      establishments.value = res.data
      alert("Estabelecimento salvo com sucesso!")
    })
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
