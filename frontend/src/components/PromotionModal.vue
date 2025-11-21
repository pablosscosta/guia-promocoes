<template>
  <transition name="fade-scale">
    <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div class="bg-white rounded-lg shadow-lg w-full max-w-lg p-6 transform transition-all duration-300">
        <h2 class="text-2xl font-bold mb-4">Cadastrar Promoção</h2>

        <!-- Título -->
        <input v-model="title" type="text" placeholder="Título"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-green-500" />

        <!-- Descrição -->
        <textarea v-model="description" placeholder="Descrição"
                  class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-green-500"></textarea>

        <!-- Estabelecimento -->
        <div class="mb-3">
          <p class="font-semibold mb-2">Estabelecimento</p>
          <div class="border rounded p-2 max-h-40 overflow-y-auto">
            <label v-for="est in establishments" :key="est.id" class="flex items-center space-x-2 mb-2">
              <input type="radio"
                     :value="est.id"
                     v-model="selectedEstablishment"
                     class="form-radio h-4 w-4 text-green-600" />
              <span>{{ est.name }}</span>
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
                  class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700 transition-colors"
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

const title = ref("");
const description = ref("");
const selectedEstablishment = ref<number|null>(null);
const establishments = ref<{ id: number; name: string }[]>([]);
const loading = ref(false);

onMounted(async () => {
  const res = await axios.get("establishments/");
  establishments.value = res.data;
});

function closeModal() {
  emit("close");
}

async function submitForm() {
  loading.value = true;
  try {
    const payload = {
      title: title.value,
      description: description.value,
      establishment: selectedEstablishment.value,
    };
    await axios.post("promotions/", payload);
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
