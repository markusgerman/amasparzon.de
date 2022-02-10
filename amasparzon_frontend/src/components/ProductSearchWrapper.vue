<template>
    <section class="page-section ProductSearchWrapper bg-quinary" id="sparen">
        <div class="container">
            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Jetzt Vergleichen</h2>
            <div class="row justify-content-center">
                <ProductSearch />
            </div>
        </div>
    </section>
</template>

<script>
import ProductSearch from './ProductSearch.vue'

export default {
    components: { ProductSearch,}

}
</script>

<style scoped>
.page-section {
  padding: 6rem 0;
}
.page-section .page-section-heading {
  font-size: 2.25rem;
  line-height: 2rem;
}
@media (min-width: 992px) {
  .page-section .page-section-heading {
    font-size: 3rem;
    line-height: 2.5rem;
  }
}
</style>