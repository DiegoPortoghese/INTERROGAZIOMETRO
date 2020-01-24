<template>
  <div>
    <Navbar />
    <Nuxt />
    <Footer />
  </div>
</template>

<script>
import Navbar from './partials/nav'
import Footer from './partials/footer'

export default {
  components:{
    Navbar,
    Footer
  }
}
</script>

<style>

</style>
