<template>

  <div class="messages">
    <Topnavbar />
    <div class="container d-flex align-items-center flex-column">
      <div class="alert alert-danger" role="alert">
        <h4 class="alert-heading">Schade!</h4>
        <p> Wir haben deine E-Mail aus unserem System entfernt. 
        </p>
        <hr>
        <p class="mb-0"> Wir hoffen du kommst bald zu uns zurück.</p>
      </div>
      <router-link to="/"> Zurück zu amasparzon </router-link>
    </div>

    <Footer class="bottom" />
  </div>
</template>

<script>

import Topnavbar from '../components/Topnavbar.vue';
import Footer from '../components/Footer.vue';

export default {
  components: { Topnavbar, Footer },

  props: ['message'],
}
</script>

<style scoped>
.bottom{
  position: fixed;
  bottom: 0;
  width: 100%;
}

.container {
    padding: 6rem 0;
}

</style>