<template>
  <div class="card-content">
    <h1 v-if="isLoading">Fetching data...</h1>
    <img src="../assets/logo.gif" v-if="isLoading">
    <LineChart
      :points="points"
      :labels="labels"
      v-if="!isLoading"
      :label="label"
    />
  </div>
</template>

<script>
import axios from 'axios'
import LineChart from '@/components/LineChart'

// function to map the data returned to what can be consumed by chart.js
const toPoints = (prices, attr) => prices.map(price => price[attr])

// function to get the labels which can be consumed by chart.js
const getLabels = (
  prices,
  showDate = true,
  showTime = false
) => prices.map(price => {
  let time = new Date(price.date * 1000)
  const res = []
  if (showDate) {
    res.push(time.toLocaleDateString('zh-Hans-CN'))
  }
  if (showTime) {
    res.push(time.toLocaleTimeString('en-GB'))
  }
  return res.join(' ')
})

const getLastTime = (prices) => {
  const lastTime = new Date(prices[prices.length - 1].date * 1000)
  return lastTime.toLocaleDateString('zh-Hans-CN') + ' ' + lastTime.toLocaleTimeString('en-GB')
}

export default {
  components: {
    LineChart
  },
  props: {
    requestParams: {
      type: Object,
      default: () => {}
    }
  },
  data () {
    return {
      isLoading: true,
      count: 0, // future use
      points: [],
      labels: [],
      error: null,
      label: '',
      lastTime: ''
    }
  },
  mounted () {
    const params = this.requestParams
    const { target, against } = params
    axios.get('api/price', {
      params
    }).then(res => {
      this.count = res.data.count
      this.labels = getLabels(res.data.result)
      this.points = toPoints(res.data.result, 'high') // TODO: think about massage data here or in Scatter Components
      this.lastTime = getLastTime(res.data.result)
      this.label = `${target} | ${against} fetched at ${this.lastTime}`
      this.isLoading = false // flag this at last for conditional renderring, don't render before the data is available
    }).catch(err => {
      this.error = err.message
    })
  },
  destroyed () {
    // console.log('destroyed') // placeholder
  }
}
</script>
