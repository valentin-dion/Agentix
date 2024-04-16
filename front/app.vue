<template>
  <div>
    <!-- Top menu with SOTA flat design and dark theme, added text thickness and shadow -->
    <nav class="bg-gray-900 text-gray-200 p-4 shadow-lg">
      <ul class="flex space-x-4">
        <li v-for="page in pages" :key="page.id">
          <!-- Subtle hover effect without compromising flat design, thicker text, and shadow -->
          <NuxtLink :to="page.path" class="hover:bg-gray-700 p-2 rounded transition-colors duration-150 font-semibold shadow"> {{ page.title }}</NuxtLink>
        </li>
      </ul>
    </nav>
    <!-- Content area rendered by Nuxt, adjusted for Nuxt 3 -->
    <NuxtPage />
  </div>
</template>

<script setup>
setTimeout(() => {
  // Create a new script element
  const script = document.createElement('script');

  // Set the source of the script to the Tailwind CDN
  script.src = "https://cdn.tailwindcss.com";

  // Append the script to the body of the document
  document.body.appendChild(script);

  // Optional: Log to console when the script is loaded
  script.onload = () => {
    console.log("Tailwind CSS has been loaded successfully!");
  };

  // Optional: Handle loading errors
  script.onerror = () => {
    console.error("Failed to load Tailwind CSS from CDN.");
  };
}, 100); // The timeout delay in milliseconds (1000 ms = 1 second)

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
