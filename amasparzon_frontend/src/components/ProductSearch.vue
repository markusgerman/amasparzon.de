<template>
  <div>
    <input type="url" id="amazonlink" name="amazonlink" @paste="onPaste" v-model="amazonlink" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      amazonlink: "",
    };
  },

  methods: {
    onPaste(evt) {
      const url = evt.clipboardData
        .getData("text")
        .replace("https://www.amazon.de", "");
      this.$router.push(url);
    },
  },
};
</script>

<style>
</style>