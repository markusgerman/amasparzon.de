<template>
  <div class="product-view">

    <div v-if="product_available == true">
      <div class="product">
        <div class="product-name" id="productname">{{ productname }}</div>
        <img class="product-image" :src="productimage" alt="productimage" />
        <div class="product-price" id="productprice">{{ productprice }}</div>
      </div>
      <save-product></save-product>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SaveProduct from './SaveProduct.vue';

export default {
  components: { SaveProduct },
  name: "ProductInformation",
  mounted() {
    if (this.$route.fullPath != "/"){
      this.GetAmazonProductAsync(this.$route.fullPath);
    }
  },
  data() {
    return {
      amazonlink: "",
      productname: "",
      productimage: "",
      productprice: "",
      product_available: false,
    };
  },
  methods: {
    onPaste(evt) {
      this.GetAmazonProductAsync(evt.clipboardData.getData("text").replace("https://www.amazon.de/", ""));
    },  

    async GetAmazonProductAsync(product_resource) {
      await axios.get(`api/products/${product_resource}`).then((response) => {
        this.productname = response.data.name;
        this.productimage = response.data.image;
        this.productprice = response.data.price;
        this.product_available = true;
      },);
    },
  },
};
</script>

<style>

.product-view{
  background-color: #f5f5f5;
}



</style>