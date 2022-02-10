<template>
  <section class="page-section productsearch" id="sparen">
    <p> Füge hier dein Produkt ein </p>
    <div class="input-group flex">
      <input type="url" id="amazonlink" name="amazonlink" class="form-control" @paste="onPaste" v-model="amazonlink" />
      <button v-on:click="resetinput()" type="button" class="btn-close btn" aria-label="Close"></button>
    </div>

    <div class="alert alert-danger" role="alert" v-if="error_message">
        {{ error_message }}
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      amazonlink: "",
      error_message: "",
    };
  },

  methods: {
    resetinput() {
      this.amazonlink = "";
    },

    onPaste(evt) {
      if (!evt.clipboardData.getData("text").includes("amazon.de")) {
        this.error_message = "Bitte geben Sie eine gültiges Produkt ein.";
        return;
      }
      const url = evt.clipboardData
        .getData("text")
        .replace("https://www.amazon.de", "");
      this.$router.push(url);
    },
  },
};
</script>

<style scoped>

.btn-close{
  margin: 10px;
}

.alert{
  width: 50%;
  margin: auto;
  margin-top: 10px;
}

.form-control{
  caret-color: transparent;
}

</style>