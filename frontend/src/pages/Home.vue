<template>
  <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)] p-4">
    <h1 class="text-5xl font-extrabold text-blue-700 mb-6 text-center">Bem-vindo ao Guia de Promoções!</h1>
    <p class="text-xl text-gray-700 mb-8 text-center max-w-2xl">
      Descubra as melhores promoções e ofertas dos seus estabelecimentos favoritos na cidade.
    </p>
    <div class="flex space-x-4">
      <router-link to="/establishments" class="px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 transition-colors duration-300">
        Ver Estabelecimentos
      </router-link>
      <router-link to="/promotions" class="px-6 py-3 bg-green-600 text-white font-semibold rounded-lg shadow-md hover:bg-green-700 transition-colors duration-300">
        Ver Promoções
      </router-link>
    </div>
  </div>
</template>

<script setup>
</script>