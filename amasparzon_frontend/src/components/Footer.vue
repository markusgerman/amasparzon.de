<template>
  <footer class="footer text-center bg-secondary">
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <a href="impressum" class="t">Impressum</a><br>
          <a href="datenschutz" class="t">Datenschutz</a>
        </div>
        <div class="col-sm">
          <h4 class="text-uppercase mb-4">Social Media</h4>
          <a href ="https://github.com/markusgerman/amasparzon.de/"> <i class="bi bi-github"></i></a>
        </div>
        <div class="col-sm">© {{ new Date().getFullYear() }} Markus German</div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style scoped>
.footer {
  padding-top: 2rem;
  padding-bottom: 2rem;
  color: #fff;
}

.bi{
  font-size: 20px;
  text-align: center;
  text-decoration: none;
}


</style>