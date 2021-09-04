<template>
    <div class="product-view">
        <label for="amazon-link">Hier Amazon Link einfügen</label>
        <input type="url" id="amazonlink" name="amazonlink" v-model="amazonlink">
        
        <div class="product">
            <div class="product-name"></div>
            <div class="product-image"></div>
            <div class="product-information"></div>
        </div>

        <label for="email">E-Mail-Adresse</label>
        <input type="email" id="email" name="email" v-model="email">
    </div>
</template>

<script>
export default {
    name: 'ProductInformation',

    data() {
        return {
            amazonlink : "",
            email : ""
        }
    },

    methods : {
        getAmazonProduct(){
            return this.amazonlink
        }
    }
}


</script>

<style>

</style>