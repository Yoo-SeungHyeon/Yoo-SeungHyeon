import { createRouter, createWebHistory } from 'vue-router'

import ChatView from '@/views/ChatView.vue'
import PromtreeView from '@/views/PromtreeView.vue'
import PixelView from '@/views/PixelView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: ChatView },
    { path: '/promtree', component: PromtreeView },
    { path: '/pixel', component: PixelView }
  ],
})

export default router
