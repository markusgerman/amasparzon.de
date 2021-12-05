<template>
  <div class="messages">
      <div class="message">
        {{ message }}
      </div>

      <router-link to="/">Home</router-link>
  </div>
</template>

<script>
export default {
    props: ['message'],
}
</script>

<style>

</style>