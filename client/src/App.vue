<template>
  <div id="app">
    <img src="./assets/logo.gif">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="sass" src="bulma"></style>
<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  color: #333;
  margin-top: 60px;
}
</style>
