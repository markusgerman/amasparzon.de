<template>
  <div>
      <Topnavbar />
      blabla willkommen auf amasparzon 

      <ProductSearch />
  </div>
</template>

<script>
// @ is an alias to /src
import Topnavbar from '../components/Topnavbar.vue'
import ProductSearch from '../components/ProductSearch.vue'

export default {
  name: 'Home',
  components: {
    Topnavbar,
    ProductSearch
  }
}
</script>
