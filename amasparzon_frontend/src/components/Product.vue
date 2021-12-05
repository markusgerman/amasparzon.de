<template>

    <div class="product">
        <div class="lds-dual-ring" v-if="loading"></div>
        <div class="product-card" v-else>
            <div class="product-name" id="productname">{{ productdata.name }}</div>
            <img class="product-image" :src="productdata.image" alt="productimage" />
            <div class="product-price" id="productprice">{{ productdata.price }}</div>
        </div>  
    </div>
</template>

<script>
import axios from "axios";

export default {
    data () {
        return {
            loading: false,
            productdata: [],
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
        }).catch((error) => {
            console.log(error);
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

.lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
}

.lds-dual-ring::after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #fff;
    border-color: black transparent black transparent;
    animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}


</style>