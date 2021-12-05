<template>

    <div class="product">
        <LoadingSpinner v-if="loading" />
        <div class="product-card" v-if ="loading == false && productavailable == true">
            <div class="product-name" id="productname">{{ productdata.name }}</div>
            <img class="product-image" :src="productdata.image" alt="productimage" />
            <div class="product-price" id="productprice">{{ productdata.price }}</div>
            <SaveProduct :productdata="productdata"></SaveProduct>
        </div> 
        <div class="product-not-available" v-if="productavailable == false">
            Produkt nicht vorhanden
            <router-link to="/">Home</router-link>
        </div>

        


    </div>
</template>

<script>
import axios from "axios";
import SaveProduct from "./SaveProduct.vue";
import LoadingSpinner from "./LoadingSpinner.vue";

export default {
    components: { SaveProduct, LoadingSpinner},
    data () {
        return {
            loading: false,
            productdata: [],
            productavailable : true,
        }
    },
    mounted() {
      this.loadProduct(this.$route.fullPath);
  },
  methods: {
      async loadProduct(product_resource) {
        this.loading = true;

        await axios.get(`api/products/${product_resource}`).then((response) => {
            this.productdata = response.data;
            this.productdata['link'] = product_resource;
            this.productavailable = true;

        }).catch((error) => {
            this.productavailable = false;
        });
        this.loading = false;
      }
  }
}
</script>

<style>
.product {
    background-color: #f5f5f5;
}
</style>