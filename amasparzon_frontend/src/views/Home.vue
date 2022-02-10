<template>
  <div class="home">
      <Topnavbar />

      <Header />

      <ProductSearchWrapper />

      <SectionTutorial />

      <About />

      <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Topnavbar from '../components/Topnavbar.vue'
import ProductSearchWrapper from '../components/ProductSearchWrapper.vue'
import Header from '../components/Header.vue'
import SectionTutorial from '../components/SectionTutorial.vue'
import About from '../components/About.vue'
import Footer from '../components/Footer.vue'

export default {
  name: 'Home',
  components: {
    Topnavbar,
    ProductSearchWrapper,
    Header,
    SectionTutorial,
    About,
    Footer,
  }
}
</script>

<style scoped>

.home {
  overflow-x: hidden;
}

@media screen and (max-width: 768px) {
    .home { padding-top: 50px; }
}


body {
  font-family: "Times New Roman", Times, serif;
}

</style>
