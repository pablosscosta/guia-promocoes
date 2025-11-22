<template>
  <transition name="fade-scale">
    <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div class="bg-white rounded-lg shadow-lg w-full max-w-lg p-6 transform transition-all duration-300">
        <h2 class="text-2xl font-bold mb-4">Cadastrar Estabelecimento</h2>

        <!-- Nome -->
        <input v-model="name" type="text" placeholder="Nome"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-blue-500" />

        <!-- Telefone -->
        <input v-model="phone" type="text" placeholder="Telefone"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-blue-500" />

        <!-- Endereço -->
        <input v-model="address" type="text" placeholder="Endereço"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-blue-500" />

        <!-- Categorias -->
        <div class="mb-3">
          <p class="font-semibold mb-2">Categorias</p>
          <div class="border rounded p-2 max-h-40 overflow-y-auto">
            <label v-for="cat in categories" :key="cat.id" class="flex items-center space-x-2 mb-2">
              <input type="checkbox"
                     :value="cat.id"
                     v-model="selectedCategories"
                     class="form-checkbox h-4 w-4 text-blue-600" />
              <span>{{ cat.name }}</span>
            </label>
          </div>
        </div>

        <!-- Botões -->
        <div class="flex justify-end space-x-2 mt-4">
          <button @click="closeModal"
                  class="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400 transition-colors">
            Cancelar
          </button>
          <button @click="submitForm"
                  class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
                  :disabled="loading">
            <span v-if="loading">Salvando...</span>
            <span v-else>Salvar</span>
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

const emit = defineEmits(["close", "saved"]);

const name = ref("");
const phone = ref("");
const address = ref("");
const selectedCategories = ref<number[]>([]);
const categories = ref<{ id: number; name: string }[]>([]);
const loading = ref(false);

onMounted(async () => {
  const res = await axios.get("categories/");
  categories.value = res.data;
});

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
    await axios.post("establishments/", payload);
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
