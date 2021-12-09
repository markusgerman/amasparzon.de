<template>
  <section class="page-section bg-quinary" id="about">
    <div class="container">
      <!-- About Section Heading-->
      <h2 class="page-section-heading text-center text-uppercase text-secondary ">
        Über uns
      </h2>

      <div class="container">
          <div class="row text-left">
            <div class="col-sm">
              <i class="bi bi-check"></i> Vergleiche Preise und Angebote<br>
              <i class="bi bi-check"></i> Finde den günstigsten Preis<br>
              <i class="bi bi-check"></i> Werde Teil unserer aufstrebenden Sparcommunity<br>
              <i class="bi bi-check"></i> Erhalte exklusive Sparangebote<br>
              <i class="bi bi-check"></i> Und das alles kostenlos<br>
            </div>
            <div class="col-sm">
              <p>
              Amasparzon ist ein Vergleichsportal für Online-Angebote. Erhalte mit unserem Angebot exklusive Sparangebote, 
              die dir dabei helfen, bei deinem Einkauf zu erfolgreich sparen. Das alles kostenlos, unverbindlich und ohne Anmeldung. 
              Gib einfach dein Angebot in die Suche ein und finde den günstigsten Preis.
              Werde Teil unserer Sparcommunity und erhalkte exklusive Angebote per E-Mail.
              Und das alles kostenlos und ohne Anmeldung.
              </p>
            </div>
          </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {};
</script>

<style scoped>

.text-left{
  text-align: justify;
  text-justify: inter-word;
  font-size: 1vw;
}

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