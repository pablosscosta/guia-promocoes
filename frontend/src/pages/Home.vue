<template>
  <div class="flex flex-col lg:flex-row min-h-screen">
    
    <!-- Coluna esquerda: imagem + overlay + card -->
    <section class="relative flex justify-center items-center w-full lg:w-1/2 bg-cover bg-center min-h-[300px] lg:min-h-screen"
             style="background-image: url('/bar-night.png')">
      
      <!-- Overlay escuro -->
      <div class="absolute inset-0 bg-black/50"></div>
      
      <!-- Card -->
      <div class="relative z-10 bg-white/90 p-6 lg:p-8 rounded-lg shadow-lg max-w-md text-center m-4">
        <h1 class="text-2xl lg:text-4xl font-extrabold text-primary-700 mb-4 lg:mb-6">
          Guia de Promoções
        </h1>
        <p class="text-base lg:text-lg text-neutral-dark mb-6 lg:mb-8">
          Descubra as melhores promoções e ofertas dos seus estabelecimentos favoritos na cidade.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link to="/establishments"
                       class="px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors text-center">
            Ver Estabelecimentos
          </router-link>
          <router-link to="/promotions"
                       class="px-6 py-3 bg-success-600 text-white rounded-lg hover:bg-success-700 transition-colors text-center">
            Ver Promoções
          </router-link>
        </div>
      </div>
    </section>
    
    <!-- Coluna direita: gradiente + informativo + botões -->
    <section class="flex flex-col justify-center items-center w-full lg:w-1/2 bg-gradient-to-br from-neutral-light via-white to-primary-50 p-8 lg:p-10 shadow-inner text-center">
      <h2 class="text-xl lg:text-2xl font-bold text-neutral-dark mb-4">
        Quer cadastrar estabelecimentos ou promoções?
      </h2>
      <p class="text-neutral-dark/80 mb-6">
        É fácil! Basta realizar login ou criar sua conta para começar.
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <router-link to="/login"
                     class="px-5 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors text-center">
          Login
        </router-link>
        <router-link to="/register"
                     class="px-5 py-2 bg-secondary-600 text-white rounded-lg hover:bg-secondary-700 transition-colors text-center">
          Cadastro
        </router-link>
      </div>
    </section>
  </div>
</template>
