<template>
  <div>
    <h1>cointracker api/price test</h1>
    <p>{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'test',
  data () {
    return {
      price: [],
      error: null
    }
  },

  created () {
    console.log('created') // eslint-disable-line
    axios.get('http://localhost/api/price')
      .then((response) => {
        this.price = response.data
        console.log(this.price) // eslint-disable-line
      })
      .catch((e) => {
        this.error = e.message
        console.log(this.error) // eslint-disable-line
      })
  }
}
</script>
