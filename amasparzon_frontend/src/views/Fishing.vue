<template>
    <div>
        <Topnavbar/>
        <Product/>

        

        <Footer class="bottom" />

    </div>
</template>

<script>
import Topnavbar from '../components/Topnavbar.vue'
import Product from '../components/Product.vue'
import Footer from '../components/Footer.vue'

export default {
  components: { Topnavbar, Product, Footer},
}

</script>

<style scoped>
/* Footer to bottom*/
.bottom{
  position: fixed;
  bottom: 0;
  width: 100%;
}

</style>