<template>
  <div class="home">
    <ProductInformation />
  </div>
</template>

<script>
// @ is an alias to /src
import ProductInformation from '@/components/ProductInformation.vue'

export default {
  name: 'Home',
  components: {
    ProductInformation
  }
}
</script>
