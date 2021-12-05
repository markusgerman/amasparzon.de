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

  props: ['productdata'],

  data() {
    return {
      email: ""
    };
  },

  methods: {
    async SaveProductAndMail() {
    
      const price = this.productdata.price.replace("€", "").replace(",", ".");

      await axios.post(`api/products/`, 
      {
        name: this.productdata.name,
        link : this.productdata.link,
        image : this.productdata.image,
        user : this.email,
        price_set : [{"price" : price}]
      }
      );
    },
  },
}
</script>

<style>

</style>