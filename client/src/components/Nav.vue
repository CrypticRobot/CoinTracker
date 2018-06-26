<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="./">
        <img src="../assets/logo.png" alt="CoinTracker" width="30" height="30">
        CoinTracker
      </a>
    </div>
    <div class="navbar-start">
      <a
        class="navbar-item"
        v-for="route of routes"
        :key="route.label"
        :href="route.href">
        {{route.label}}
      </a>
    </div>
  </nav>
</template>

<script>

const ROUTES = [
  {
    label: 'Price',
    href: '/'
  },
  {
    label: 'Status',
    href: '/status'
  }
]

export default {
  name: 'Nav',
  data () {
    return {
      routes: ROUTES
    }
  }
}
</script>
