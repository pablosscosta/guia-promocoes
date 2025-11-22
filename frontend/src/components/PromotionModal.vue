<template>
  <transition name="fade-scale">
    <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div class="bg-white rounded-lg shadow-lg w-full max-w-lg p-6 transform transition-all duration-300">
        <h2 class="text-2xl font-bold mb-4">
          {{ isEdit ? "Editar Promoção" : "Cadastrar Promoção" }}
        </h2>

        <!-- Título -->
        <input v-model="title" type="text" placeholder="Título"
               class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-green-500" />

        <!-- Descrição -->
        <textarea v-model="description" placeholder="Descrição"
                  class="w-full border rounded p-2 mb-3 focus:ring-2 focus:ring-green-500"></textarea>

        <!-- Estabelecimento -->
        <div class="mb-3">
          <p class="font-semibold mb-2">Estabelecimento</p>
          <select v-model="selectedEstablishment"
                  class="w-full border rounded p-2 focus:ring-2 focus:ring-green-500">
            <option v-for="est in establishments" :key="est.id" :value="est.id">
              {{ est.name }}
            </option>
          </select>
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
            <span v-else>{{ isEdit ? "Salvar alterações" : "Salvar" }}</span>
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from "vue";
import axios from "axios";

const emit = defineEmits(["close", "saved"]);
const props = defineProps<{
  promotion?: {
    id: number;
    title: string;
    description: string;
    establishment: number;
  };
}>();

const isEdit = computed(() => !!props.promotion);

const title = ref("");
const description = ref("");
const selectedEstablishment = ref<number | null>(null);
const establishments = ref<{ id: number; name: string }[]>([]);
const loading = ref(false);

onMounted(async () => {
  const res = await axios.get("establishments/");
  establishments.value = res.data;
});

const hydrateFormFromProps = () => {
  if (!props.promotion) return;
  title.value = props.promotion.title;
  description.value = props.promotion.description;
  selectedEstablishment.value = props.promotion.establishment;
};

onMounted(hydrateFormFromProps);
watch(() => props.promotion, hydrateFormFromProps);

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

    if (isEdit.value && props.promotion) {
      await axios.put(`promotions/${props.promotion.id}/`, payload);
    } else {
      await axios.post("promotions/", payload);
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
