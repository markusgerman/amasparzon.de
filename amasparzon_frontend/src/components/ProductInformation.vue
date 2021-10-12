<template>
  <div class="product-view">
    <label for="amazon-link">Hier Amazon Link einfügen</label>
    <input
      type="url"
      id="amazonlink"
      name="amazonlink"
      @paste="onPaste"
      v-model="amazonlink"
    />

    <div v-if="productimage">
      <div class="product">
        <div class="product-name" id="productname">{{ productname }}</div>
        <img class="product-image" :src="productimage" alt="productimage" />
        <div class="product-price" id="productprice">{{ productprice }}</div>
      </div>

        
      <label for="email">E-Mail-Adresse</label>
      <input type="email" id="email" name="email" v-model="email" />
      <p> Sie werden benachrichtigt sobald sich der Preis ändert </p>
    </div>
    
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductInformation",
  data() {
    return {
      amazonlink: "",
      email: "",
      productname: "",
      productimage: "",
      productprice: "",
    };
  },
  methods: {
    onPaste(evt) {
      this.GetAmazonProductAsync(
        evt.clipboardData.getData("text").replace("https://www.amazon.com/", "")
      );
    },

    async GetAmazonProductAsync(product_resource) {
      await axios.get(`api/products/${product_resource}`).then((response) => {
        this.productname = response.data.name;
        this.productimage = response.data.image;
        this.productprice = response.data.price;
      });
    },
  },
};
</script>

<style>
</style>