<template>
  <div id="topnav">
  <ul>
    <li><router-link to="foo">Anmelden</router-link></li>
    <li><router-link to="home">Home</router-link></li>
  </ul>
</div>
</template>

<script>
export default {
}
</script>

<style>

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: right;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}

</style>