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

  fetchPages();
});

// Mock function to simulate fetching pages
function fetchPages() {
  // Simulating a delay and response from an API
  setTimeout(async () => {
    pages.value = [ {id:1,title:'index',path:'/'}, ...(await back('all_pages')).map(p=>{
      return {id:p,title:p,path:`/${p}`}
    })];
  }, 1000); // 1 second delay to mimic async API call

  setInterval(()=>{
    
  },1555)
}
</script>
