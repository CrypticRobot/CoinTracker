<template>
  <div class="container">
    <h1>cointracker api/currencies test</h1>
    <Collapse
      class="card"
      v-for="currency of currencies"
      :key="currency.target + currency.against + currency.time_unit"
    >
      <header class="card-header" slot="trigger">
        <p class="card-header-title coloumn is-centered">
          {{`${currency.target.toUpperCase()} / ${currency.against.toUpperCase()}`}}
        </p>
        <p class="card-header-title coloumn is-centered">振幅</p>
        <p class="card-header-title coloumn is-centered">
          {{`${currency.limit*currency.time_elapse} ${currency.time_unit.toUpperCase()}`}}
        </p>
      </header>
      <LineChartWrapper :requestParams="currency"/>
    </Collapse>
    <p
      class="has-text-danger"
      v-if="error"
    >
      {{ error }}
    </p>
  </div>
</template>

<script>
import axios from 'axios'
import Collapse from '@/components/Collapse'
import LineChartWrapper from '@/components/LineChartWrapper'

export default {
  name: 'App',
  components: {
    Collapse,
    LineChartWrapper
  },
  data () {
    return {
      currencies: [],
      error: null
    }
  },
  created () {
    axios.get('/api/currencies')
      .then((response) => {
        this.currencies = response.data
      })
      .catch((e) => {
        this.error = e.message
      })
  }
}
</script>
