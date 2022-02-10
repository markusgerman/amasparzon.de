<template>

  <div class="messages">
    <Topnavbar />
    <div class="container d-flex align-items-center flex-column">
      <div class="alert alert-success" role="alert">
        <h4 class="alert-heading">Hervorragend!</h4>
        <p> Wir haben dein Produkt auf unsere Beobachtungsliste gesetzt! 
          <br>
          Du wirst nun eine Bestätigungsmail erhalten.
        </p>
        <hr>
        <p class="mb-0"> Wir melden uns, sobald der Preis deines Produktes sinkt.</p>
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