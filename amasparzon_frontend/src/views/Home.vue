<template>
  <div>
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
