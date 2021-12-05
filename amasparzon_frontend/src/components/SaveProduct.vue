<template>
  <div>
    <label for="email">E-Mail-Adresse</label>
    <input type="email" id="email" name="email" v-model="email" />
    <p> Sie werden benachrichtigt sobald sich der Preis ändert </p>

    <button @click="SaveProductAndMail">Speichern</button>
  </div>
</template>

<script>
import axios from "axios";
export default {

  data() {
    return {
      email: ""
    };
  },

  methods: {
    async SaveProductAndMail() {
      await axios.post(`api/products/`, {
        email: this.email
      });
    },
  },
}
</script>

<style>

</style>