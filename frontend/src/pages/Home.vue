<template>
  <div class="flex flex-col min-h-screen">
    <!-- Header com Login/Cadastro -->
    <header class="flex justify-end p-4 bg-gray-100 shadow">
      <router-link to="/login" class="px-4 py-2 text-gray-700 hover:text-gray-900">
        Login
      </router-link>
      <router-link to="/register" class="ml-4 px-4 py-2 bg-orange-600 text-white rounded-lg hover:bg-orange-700 transition-colors duration-300">
        Cadastro
      </router-link>
    </header>

    <!-- Hero central -->
    <main class="flex flex-col items-center justify-center flex-grow p-4">
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
    </main>
  </div>
</template>
