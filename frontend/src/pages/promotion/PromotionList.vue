<template>
  <div class="container mx-auto p-4">
    
    <!-- Título principal -->
    <h1 class="text-3xl font-bold text-neutral-dark mb-6 text-center">
      Nossas Promoções
    </h1>

    <!-- Ações principais -->
    <div class="flex justify-center mb-6 space-x-6">
      <!-- Botão cadastrar -->
      <button
        @click="openCreateModal"
        class="px-6 py-2 bg-success-600 text-white font-semibold rounded-lg shadow-md hover:bg-success-700 transition-colors duration-300"
      >
        Cadastrar Promoção
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
    <PromotionModal
      v-if="showModal"
      :promotion="selectedPromotion"
      @close="showModal = false"
      @saved="onPromotionSaved"
    />

    <!-- Mensagens de estado -->
    <p v-if="loading" class="text-center text-lg text-primary-600">
      Carregando promoções...
    </p>
    <p v-else-if="error" class="text-center text-lg text-error-600">
      Erro ao carregar promoções: {{ error?.message }}
    </p>

    <!-- Lista + barra de busca e filtro -->
    <div v-else>
      <!-- Barra de busca e filtro -->
      <div class="flex justify-center mb-6 space-x-6">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Buscar promoção..."
          class="w-full md:w-1/3 px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-600"
        />

        <select
          v-model="selectedEstablishment"
          class="px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-600"
        >
          <option value="">Todos estabelecimentos</option>
          <option
            v-for="name in uniqueEstablishmentNames"
            :key="name"
            :value="name"
          >
            {{ name }}
          </option>
        </select>
      </div>

      <!-- Lista de promoções filtrada -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="promotion in filteredPromotions"
          :key="promotion.id"
          class="bg-white rounded-lg shadow-md p-6 border-t-4 border-success-600 hover:shadow-lg transition-shadow duration-300"
        >
          <!-- Título da promoção -->
          <h2 class="text-xl font-semibold text-neutral-dark mb-2">
            {{ promotion.title }}
          </h2>
          <!-- Descrição -->
          <p class="text-neutral-dark/70 mb-1">{{ promotion.description }}</p>
          <!-- Estabelecimento -->
          <p class="text-neutral-dark mb-3">
            Estabelecimento: {{ promotion.establishment_name }}
          </p>

          <!-- Botão Editar -->
          <button
            @click="editPromotion(promotion)"
            class="px-3 py-1 bg-primary-600 text-white rounded hover:bg-warning-600"
          >
            ✏️ Editar
          </button>
          <!-- Botão Excluir -->
          <button
            @click="deletePromotion(promotion.id)"
            class="ml-2 px-3 py-1 bg-secondary-600 text-white rounded hover:bg-error-700"
          >
            🗑️ Excluir
          </button>
        </div>
      </div>

      <!-- Mensagem lista vazia -->
      <p
        v-if="!loading && !error && filteredPromotions.length === 0"
        class="text-center text-lg text-neutral-dark/60 mt-8"
      >
        Nenhuma promoção encontrada.
      </p>
    </div>
  </div>
</template>


<script setup lang="ts">
import api from '../../services/api';
import { ref, onMounted, computed } from 'vue';
import PromotionModal from '../../components/PromotionModal.vue';

const promotions = ref<any[]>([]);
const loading = ref(true);
const error = ref<Error | null>(null);
const showModal = ref(false);
const selectedPromotion = ref<any | null>(null);

// Busca e filtro (texto + estabelecimento)
const searchTerm = ref("");
const selectedEstablishment = ref("");

// Lista única de nomes de estabelecimentos
const uniqueEstablishmentNames = computed(() => {
  const set = new Set(
    promotions.value
      .map(p => p.establishment_name)
      .filter((name: string | null | undefined) => !!name)
  );
  return Array.from(set).sort();
});

// Lista filtrada
const filteredPromotions = computed(() => {
  const term = searchTerm.value.trim().toLowerCase();

  return promotions.value.filter(p => {
    const matchesSearch =
      !term ||
      (p.title && String(p.title).toLowerCase().includes(term)) ||
      (p.description && String(p.description).toLowerCase().includes(term));

    const matchesEstablishment =
      !selectedEstablishment.value ||
      p.establishment_name === selectedEstablishment.value;

    return matchesSearch && matchesEstablishment;
  });
});

onMounted(async () => {
  try {
    const response = await api.get('promotions/');
    promotions.value = response.data;
  } catch (err: any) {
    error.value = err;
    console.error("Erro ao buscar promoções:", err);
  } finally {
    loading.value = false;
  }
});

function onPromotionSaved() {
  loading.value = true;
  api.get('promotions/')
    .then(res => promotions.value = res.data)
    .catch(err => {
      error.value = err;
      console.error("Erro ao atualizar promoções:", err);
    })
    .finally(() => loading.value = false);
}

function openCreateModal() {
  selectedPromotion.value = null;
  showModal.value = true;
}

function editPromotion(promo: any) {
  selectedPromotion.value = promo;
  showModal.value = true;
}

async function deletePromotion(id: number) {
  if (!confirm("Tem certeza que deseja excluir esta promoção?")) return;
  try {
    await api.delete(`promotions/${id}/`);
    promotions.value = promotions.value.filter(p => p.id !== id);
  } catch (err) {
    console.error("Erro ao excluir promoção:", err);
    alert("Erro ao excluir promoção.");
  }
}
</script>
