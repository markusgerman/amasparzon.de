import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Fishing from '../views/Fishing.vue'
import Messages from '../views/Messages.vue'
import DeleteProfil from '../views/DeleteProfil.vue'

document.title = "amasparzon.de";

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
  },
  {
    path: '/profildelete',
    name: 'ProfilDelete',
    component: DeleteProfil,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
