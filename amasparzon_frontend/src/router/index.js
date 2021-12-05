import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Fishing from '../views/Fishing.vue'
import Messages from '../views/Messages.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    // path: "*",
    path: "/:catchAll(.*)",
    name: "Fishing",
    component: Fishing,
  },
  {
    path: '/info',
    name: 'Info',
    component: Messages,
    props : true
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
