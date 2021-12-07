<template>
  <header class="masthead text-white text-center">
        <div class="container d-flex align-items-center flex-column">
            <!-- Masthead Avatar Image-->
            <img class="masthead-avatar mb-5" src="../assets/avataaars.svg" alt="..." />
        
            <!-- Masthead Heading-->
            <h1 class="masthead-heading text-uppercase mb-0">amaSPARzon</h1>

            <!-- Masthead Subheading-->
            <div class="typewriter">
              <h3>Dein Preisvergleichsportal</h3>
            </div>

        </div>
    </header>
</template>

<script>
export default {

}
</script>


<style scoped>
.masthead{
    background-color: #1ABC9C;
}

.masthead .masthead-heading {
  font-size: 2.75rem;
  line-height: 2.75rem;
}
.masthead .masthead-subheading {
  font-size: 1.25rem;
}
.masthead .masthead-avatar {
  width: 15rem;
}

@media (min-width: 992px) {
  .masthead {
    padding-top: calc(6rem + 104px);
    padding-bottom: 6rem;
  }
  .masthead .masthead-heading {
    font-size: 4rem;
    line-height: 3.5rem;
  }
  .masthead .masthead-subheading {
    font-size: 1.5rem;
  }
}

.typewriter h3 {
  overflow: hidden;
  border-right: .15em solid orange; 
  white-space: nowrap; 
  margin: 0 auto; 
  letter-spacing: .15em;
  animation: 
    typing 1.5s steps(40, end),
    blink-caret .75s step-end;
}

/* The typing effect */
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: #2C3E50; }
}
</style>