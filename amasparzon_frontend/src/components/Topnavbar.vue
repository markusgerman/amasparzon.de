<template>
  <nav class="navbar navbar-expand-lg bg text-uppercase fixed-top" id="mainNav">
    <div class="container">
        <a class="navbar-brand" href="/">amaSPARzon</a>
        <button class="navbar-toggler text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded" href="#sparen">SPAREN</a></li>
                <li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded" href="#tutorial">Tutorial</a></li>
                <li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded" href="#kontakt">Kontakt</a></li>
            </ul>
        </div>
    </div>
  </nav>
</template>

<script>
export default {
}
</script>

<style scoped>

.bg{
  background-color: #2C3E50;
}

.navbar {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.nav-link, .navbar-brand {
  color: white;
}



</style>