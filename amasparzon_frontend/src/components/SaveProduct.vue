<template>
  <div>
    <div class="input-group mb-3" v-if="loading == false && isProductSaved == false">
      <div class="input-group-prepend">
        <span class="input-group-text" id="inputGroup-sizing-default">E-Mail Adresse</span>
      </div>
      <input class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="email" id="email" name="email" v-model="email">
       <button class="btn btn-primary" @click="SaveProductAndMail">Speichern</button>
    </div>
    
    <div class="loading" v-if ="loading == true">
      <loading-spinner/>
    </div>

    <div class="product-saved" v-if="isProductSaved == true && error == ''">
      Produkt wurde gespeichert
      <router-link to="/">Home</router-link>
    </div>

    <div class="error" v-if="error != '' ">
      {{ error }}<br>
      <router-link to="/">Home</router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import LoadingSpinner from "./LoadingSpinner.vue";
export default {
  components: { LoadingSpinner },
  props: ['productdata'],

  data() {
    return {
      email: "",
      savingSuccessful: false,
      loading: false,
      isProductSaved: false,
      error: "",
    };
  },

  methods: {
    async SaveProductAndMail() {  
      this.loading = true;
      await axios.post(`api/products/`, 
      {
        asin: this.productdata.asin,
        user : this.email,
      }).catch((error) => {
        if (error.response.status == 409) {
          this.error = "Dieses Produkt ist bereits in deiner Liste";
        } else {
          this.error = "Es ist ein Fehler aufgetreten. Probier es später erneut.";
        }
      });
      this.loading = false;
      this.isProductSaved = true;
    },
  },
}
</script>

<style>

</style>