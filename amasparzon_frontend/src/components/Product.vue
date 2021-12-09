<template>
  <div class="container d-flex align-items-center flex-column">
      
    <LoadingSpinner v-if="loading" />

    <div class="card" v-if ="loading == false && productavailable == true">
      <img class="card-img-top" :src="productdata.image" alt="Card image cap" />
      <div class="card-body">
        <h5 class="card-title">{{ productdata.name }}</h5>
        <h1 class="card-title pricing-card-title">{{ productdata.price }}</h1>
      </div>

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
  components: { SaveProduct, LoadingSpinner },
  data() {
    return {
      loading: false,
      productdata: [],
      productavailable: true,
    };
  },
  mounted() {
    this.loadProduct(this.$route.fullPath);
  },
  methods: {
    async loadProduct(product_resource) {
      this.loading = true;

      await axios
        .get(`api/products/${product_resource}`)
        .then((response) => {
          this.productdata = response.data;
          this.productdata["link"] = product_resource;
          this.productavailable = true;
        })
        .catch((error) => {
          this.productavailable = false;
        });
      this.loading = false;
    },
  },
};
</script>

<style scoped>
.container {
    padding: 6rem 0;
}

.card{
  padding: 1rem;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

.card-img-top{
  width: 150px;
  height: auto;
}


</style>