<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold text-neutral-dark mb-6 text-center">
      Dashboard do Estabelecimento
    </h1>

    <!-- Botão para abrir modal -->
    <button @click="openCreateModal"
            class="mb-4 px-4 py-2 bg-primary-600 text-white rounded hover:bg-primary-700">
      + Nova Promoção
    </button>

    <!-- Lista de promoções -->
    <section class="bg-white rounded-lg shadow-md p-6 border-t-4 border-success-600 mb-6">
      <h2 class="text-xl font-semibold mb-4">Minhas Promoções</h2>
      <ul v-if="promotions.length > 0">
        <li v-for="promo in promotions" :key="promo.id" class="flex justify-between items-center p-2 border-b">
          <div>
            <p class="font-bold">{{ promo.title }}</p>
            <p class="text-sm text-neutral-dark/70">{{ promo.description }}</p>
          </div>
          <div class="flex gap-2">
            <button @click="openEditModal(promo)" class="btn btn-primary">Editar</button>
            <button @click="deletePromotion(promo.id)" class="btn btn-warning">Excluir</button>
          </div>
        </li>
      </ul>
      <p v-else class="text-neutral-dark/70">Nenhuma promoção encontrada.</p>
    </section>

    <!-- Perfil -->
    <section class="bg-white rounded-lg shadow-md p-6 border-t-4 border-primary-600">
      <h2 class="text-xl font-semibold mb-4">Meu Perfil</h2>
      <p class="text-neutral-dark/70">Usuário: {{ user?.username }}</p>
      <p class="text-neutral-dark/70">Perfil: {{ user?.role }}</p>
      <p v-if="establishment" class="text-neutral-dark/70">
        Estabelecimento: {{ establishment.name }} - {{ establishment.address }}
      </p>
      <button @click="logout" class="btn btn-danger mt-4">Logout</button>
    </section>

    <!-- Modal de promoções -->
    <PromotionModal
      v-if="showPromotionModal"
      :promotion="selectedPromotion"
      @close="closeModal"
      @saved="loadPromotions"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import api from "../../services/api";
import PromotionModal from "../../components/PromotionModal.vue";

const user = ref<any>(null);
const establishment = ref<any>(null);
const promotions = ref<any[]>([]);
const loading = ref(true);
const error = ref<any>(null);

// controle do modal
const showPromotionModal = ref(false);
const selectedPromotion = ref<any>(null);

onMounted(async () => {
  await loadUser();
  await loadPromotions();
});

async function loadUser() {
  try {
    const { data: me } = await api.get("/auth/me/details/");
    user.value = { id: me.id, username: me.username, role: me.role };
    establishment.value = me.establishments?.[0] || null;
  } catch (err: any) {
    error.value = err;
    console.error("Erro ao carregar detalhes:", err);
  } finally {
    loading.value = false;
  }
}

async function loadPromotions() {
  try {
    const { data } = await api.get("/promotions/");
    promotions.value = data;
  } catch (err) {
    console.error("Erro ao carregar promoções:", err);
  }
}

function openCreateModal() {
  selectedPromotion.value = null;
  showPromotionModal.value = true;
}

function openEditModal(promo: any) {
  selectedPromotion.value = promo;
  showPromotionModal.value = true;
}

function closeModal() {
  showPromotionModal.value = false;
}

async function deletePromotion(id: number) {
  try {
    await api.delete(`/promotions/${id}/`);
    await loadPromotions();
  } catch (err) {
    console.error("Erro ao excluir promoção:", err);
  }
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "/login";
}
</script>
