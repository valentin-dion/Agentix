<template>
  <div>
    <!-- Top menu with SOTA flat design and dark theme, added text thickness and shadow -->
    <nav class="bg-gray-900 text-gray-200 p-4 shadow-lg">
      <ul class="flex space-x-4">
        <li v-for="page in pages" :key="page.id">
          <!-- Apply a different style for the active page -->
          <NuxtLink :to="page.path" class="p-2 rounded transition-colors duration-150 font-semibold shadow"
                    :class="{'bg-gray-700 hover:bg-gray-600': isActivePage(page.path), 'hover:bg-gray-700': !isActivePage(page.path)}">
            {{ page.title }}
          </NuxtLink>
        </li>
      </ul>
    </nav>
    <!-- Content area rendered by Nuxt, adjusted for Nuxt 3 -->
    <NuxtPage />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useNuxtApp } from '#app'; // Use Nuxt 3's useNuxtApp composable

const pages = ref([]);
const nuxtApp = useNuxtApp();
const route = nuxtApp.$router.currentRoute; // Access current route using Nuxt 3's way

// Ensure route is accessed after it's defined and check if route and route.path are defined
const isActivePage = (pagePath) => {
  return route.value && route.value.path ? route.value.path === pagePath : false;
};

// Simulate fetching pages on component mount
onMounted(() => {
  fetchPages();
});

// Mock function to simulate fetching pages
function fetchPages() {
  // Simulating a delay and response from an API
  setTimeout(() => {
    pages.value = [
      { id: 1, title: 'Home', path: '/' },
      { id: 2, title: 'About', path: '/about' },
      { id: 3, title: 'Contact', path: '/contact' }
    ];
  }, 1000); // 1 second delay to mimic async API call
}
</script>
