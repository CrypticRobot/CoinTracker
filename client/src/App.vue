<template>
  <div id="app">
    <Nav />
    <img src="./assets/logo.gif">
    <router-view/>
  </div>
</template>

<script>
import Nav from '@/components/Nav.vue'

export default {
  name: 'App',
  components: {
    Nav
  }
}
</script>

<style lang="sass" src="bulma" />
<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  color: #333;
}
</style>
