<template>
  <div>
    <!-- Top menu with SOTA flat design and dark theme -->
    <nav class="bg-gray-900 text-gray-200 p-4 shadow-md">
      <ul class="flex space-x-4">
        <li v-for="page in pages" :key="page.id">
          <!-- Subtle hover effect without compromising flat design -->
          <NuxtLink :to="page.path" class="hover:bg-gray-700 p-2 rounded transition-colors duration-150">{{ page.title }}</NuxtLink>
        </li>
      </ul>
    </nav>
    <!-- Content area rendered by Nuxt, adjusted for Nuxt 3 -->
    <NuxtPage />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const pages = ref([]);

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
