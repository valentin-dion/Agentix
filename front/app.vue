<template>
  <div>
    <!-- Top menu -->
    <nav>
      <ul>
        <li v-for="page in pages" :key="page.id">
          <NuxtLink :to="page.path">{{ page.title }}</NuxtLink>
        </li>
      </ul>
    </nav>
    <!-- Content area rendered by Nuxt -->
    <Nuxt />
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
