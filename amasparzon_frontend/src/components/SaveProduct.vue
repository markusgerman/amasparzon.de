<template>
  <div>
    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="inputGroup-sizing-default">E-Mail Adresse</span>
      </div>
      <input class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="email" id="email" name="email" v-model="email">
    </div>
    <p> Sie werden benachrichtigt sobald sich der Preis ändert </p>
    <button class="btn btn-primary" @click="SaveProductAndMail">Speichern</button>
  </div>
</template>

<script>
import axios from "axios";
export default {

  props: ['productdata'],

  data() {
    return {
      email: "",
      savingSuccessful: false,
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

      this.$router.push({ name: 'Info', params: {message : "Wir haben Ihre E-Mail erfolgreich gespeichert."} });
    },
  },
}
</script>

<style>

</style>