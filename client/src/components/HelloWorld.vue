<template>
  <div>
    <h1>cointracker api/price test</h1>
    {{price}}
    <p>{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      price: [],
      error: null
    }
  },

  created () {
    axios.get('/api/price')
      .then((response) => {
        this.price = response.data
      })
      .catch((e) => {
        this.error = e.message
      })
  }
}
</script>
