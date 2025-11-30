<template>
  <div class="container mx-auto p-6 max-w-lg">
    <h1 class="text-3xl font-bold text-neutral-dark mb-6 text-center">
      Cadastro
    </h1>

    <!-- Ações (retornar) -->
    <div class="flex justify-center mb-6">
      <router-link
        to="/"
        class="flex items-center gap-2 px-6 py-2 bg-neutral-dark text-white font-semibold rounded-lg shadow-md hover:bg-neutral-dark/80 transition-colors duration-300"
      >
        ⬅️ Retornar
      </router-link>
    </div>

    <!-- Formulário de cadastro -->
    <form @submit.prevent="register" class="space-y-4">
      <!-- Escolha de perfil -->
      <div>
        <label class="font-semibold">Perfil</label>
        <div class="flex gap-4 mt-2">
          <label>
            <input type="radio" value="cliente" v-model="role" />
            Cliente
          </label>
          <label>
            <input type="radio" value="estabelecimento" v-model="role" />
            Estabelecimento
          </label>
        </div>
      </div>

      <!-- Campos comuns -->
      <div>
        <label>Usuário</label>
        <input v-model="username" class="w-full border rounded p-2" />
      </div>

      <div>
        <label>Senha</label>
        <input type="password" v-model="password" class="w-full border rounded p-2" />
      </div>

      <!-- Campos extras se for estabelecimento -->
      <div v-if="role === 'estabelecimento'" class="border-t pt-4 space-y-3">
        <div>
          <label>Nome do estabelecimento</label>
          <input v-model="name" class="w-full border rounded p-2" />
        </div>
        <div>
          <label>Endereço</label>
          <input v-model="address" class="w-full border rounded p-2" />
        </div>
        <div>
          <label>Telefone</label>
          <input v-model="phone_number" class="w-full border rounded p-2" />
        </div>
        <div>
          <label>Categorias</label>
          <select v-model="categories" multiple class="w-full border rounded p-2">
            <option v-for="cat in availableCategories" :key="cat.id" :value="cat.id">
              {{ cat.name }}
            </option>
          </select>
        </div>
      </div>

      <!-- Mensagem de erro -->
      <p v-if="error" class="text-error-600">{{ error }}</p>

      <!-- Botão -->
      <button class="px-6 py-2 bg-primary-600 text-white font-semibold rounded-lg shadow-md hover:bg-primary-700 transition-colors duration-300">
        Cadastrar
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import api from "../services/api";
import { useAuthStore } from "../store/auth";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const role = ref<"cliente" | "estabelecimento">("cliente");

// Campos extras para estabelecimento
const name = ref("");
const address = ref("");
const phone_number = ref("");
const categories = ref<number[]>([]);
const availableCategories = ref<{ id: number; name: string }[]>([]);

const error = ref("");
const router = useRouter();
const auth = useAuthStore();

// Carregar categorias disponíveis
onMounted(async () => {
  try {
    const { data } = await api.get("/categories/");
    availableCategories.value = data;
  } catch (err: any) {
    error.value = "Erro ao carregar categorias";
  }
});

async function register() {
  try {
    const payload: any = {
      username: username.value,
      password: password.value,
      role: role.value,
    };

    if (role.value === "estabelecimento") {
      payload.establishment = {
        name: name.value,
        address: address.value,
        phone_number: phone_number.value,
        categories: categories.value,
      };
    }

    // Cadastro
    await api.post("/auth/register/", payload);

    // Login automático
    const { data } = await api.post("/auth/login/", {
      username: username.value,
      password: password.value,
    });

    localStorage.setItem("token", data.access);
    await auth.loadUser();

    // Redirecionar conforme role
    if (role.value === "estabelecimento") {
      router.push({ name: "DashboardEstablishment" });
    } else {
      router.push({ name: "DashboardClient" });
    }
  } catch (err: any) {
    error.value = "Erro ao cadastrar usuário";
  }
}
</script>
