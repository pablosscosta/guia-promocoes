<template>
  <!-- Transição do modal -->
  <transition name="fade-scale">
    <!-- Overlay escuro -->
    <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      
      <!-- Container do modal -->
      <div class="bg-white rounded-lg shadow-lg w-full max-w-lg p-6 transform transition-all duration-300">
        
        <!-- Título do modal -->
        <h2 class="text-2xl font-bold mb-4">
          {{ isEdit ? "Editar Estabelecimento" : "Cadastrar Estabelecimento" }}
        </h2>

        <!-- Campo nome -->
        <input v-model="name" type="text" placeholder="Nome"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-primary-600" />

        <!-- Campo telefone -->
        <input v-model="phone" type="text" placeholder="Telefone"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-primary-600" />

        <!-- Campo endereço -->
        <input v-model="address" type="text" placeholder="Endereço"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-primary-600" />

        <!-- Lista de categorias -->
        <div class="mb-3">
          <p class="font-semibold mb-2">Categorias</p>
          <div class="border rounded p-2 max-h-40 overflow-y-auto">
            <label v-for="cat in categories" :key="cat.id" class="flex items-center space-x-2 mb-2">
              <input type="checkbox"
                     :value="cat.id"
                     v-model="selectedCategories"
                     class="form-checkbox h-4 w-4 text-primary-600" />
              <span>{{ cat.name }}</span>
            </label>
          </div>
        </div>

        <!-- Botões de ação -->
        <div class="flex justify-end space-x-2 mt-4">
          <!-- Botão cancelar -->
          <button @click="closeModal"
                  class="px-4 py-2 bg-neutral-light rounded hover:bg-neutral-dark/20 transition-colors">
            Cancelar
          </button>
          
          <!-- Botão salvar -->
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
import { ref, onMounted, computed, watch } from "vue";
import api from '../services/api';

const emit = defineEmits(["close", "saved"]);
const props = defineProps<{
  establishment?: {
    id: number;
    name: string;
    phone_number: string;
    address: string;
    categories: { id: number; name: string }[];
  };
}>();

const isEdit = computed(() => !!props.establishment);

const name = ref("");
const phone = ref("");
const address = ref("");
const selectedCategories = ref<number[]>([]);
const categories = ref<{ id: number; name: string }[]>([]);
const loading = ref(false);

onMounted(async () => {
  const res = await api.get("categories/");
  categories.value = res.data;
});

const hydrateFormFromProps = () => {
  if (!props.establishment) return;
  name.value = props.establishment.name;
  phone.value = props.establishment.phone_number;
  address.value = props.establishment.address;
  selectedCategories.value = (props.establishment.categories || []).map(c => c.id);
};

onMounted(hydrateFormFromProps);
watch(() => props.establishment, hydrateFormFromProps);

function closeModal() {
  emit("close");
}

async function submitForm() {
  loading.value = true;
  try {
    const payload = {
      name: name.value,
      phone_number: phone.value,
      address: address.value,
      category_ids: selectedCategories.value,
    };

    if (isEdit.value && props.establishment) {
      await api.put(`establishments/${props.establishment.id}/`, payload);
    } else {
      await api.post("establishments/", payload);
    }

    emit("saved");
    closeModal();
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.fade-scale-enter-active, .fade-scale-leave-active {
  transition: all 0.3s ease;
}
.fade-scale-enter-from, .fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>
