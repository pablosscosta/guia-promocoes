<template>
  <!-- Modal com transição -->
  <transition name="fade-scale">
    <!-- Fundo escuro -->
    <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      
      <!-- Caixa do modal -->
      <div class="bg-white rounded-lg shadow-lg w-full max-w-lg p-6">
        
        <!-- Título -->
        <h2 class="text-2xl font-bold mb-4">
          {{ isEdit ? "Editar Promoção" : "Cadastrar Promoção" }}
        </h2>

        <!-- Campos -->
        <input v-model="title" type="text" placeholder="Título"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-primary-600" />

        <textarea v-model="description" placeholder="Descrição"
                  class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-primary-600"></textarea>

        <input v-model="price" type="number" placeholder="Preço"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-primary-600" />

        <!-- Botões -->
        <div class="flex justify-end gap-2 mt-4">
          <button @click="closeModal"
                  class="px-4 py-2 bg-neutral-light rounded hover:bg-neutral-dark/20 transition-colors">
            Cancelar
          </button>
          <button @click="submitForm"
                  class="px-4 py-2 bg-primary-600 text-white rounded hover:bg-primary-700 transition-colors"
                  :disabled="loading">
            <span v-if="loading">Salvando...</span>
            <span v-else>{{ isEdit ? "Salvar alterações" : "Salvar" }}</span>
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import api from "../services/api";

// Props e emits
const emit = defineEmits(["close", "saved"]);
const props = defineProps<{ promotion?: { id: number; title: string; description: string; price: number } }>();

// Estado
const isEdit = computed(() => !!props.promotion);
const title = ref(props.promotion?.title || "");
const description = ref(props.promotion?.description || "");
const price = ref(props.promotion?.price || 0);
const loading = ref(false);

// Funções
function closeModal() {
  emit("close");
}

async function submitForm() {
  loading.value = true;
  try {
    const payload = { title: title.value, description: description.value, price: price.value };

    if (isEdit.value && props.promotion) {
      await api.put(`/promotions/${props.promotion.id}/`, payload);
    } else {
      await api.post("/promotions/", payload);
    }

    emit("saved");
    closeModal();
  } catch (err) {
    console.error("Erro ao salvar promoção:", err);
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
/* Transição */
.fade-scale-enter-active, .fade-scale-leave-active {
  transition: all 0.3s ease;
}
.fade-scale-enter-from, .fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>
