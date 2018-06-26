<template>
  <div class="columns is-centered">
      <table class="table">
        <tbody class="column">
          <tr v-if="status.last_cron">
            <th>
              Cron: <small class="has-text-danger">({{status.count_cron}})</small>
            </th>
            <td class="has-text-success">{{ tsToDate(status.last_cron.date) }}</td>
          </tr>
          <tr v-for="price in status.prices" :key="price.pair">
            <th>
              {{price.first.target}}/
              <small>{{price.first.against}}
              <span class="has-text-danger">({{price.count}})</span></small>
            </th>
            <td class="has-text-success">{{tsToDate(price.last.date)}}</td>
          </tr>
        </tbody>
      </table>
  </div>
</template>
<script>

import axios from 'axios'
import moment from 'moment'

export default {
  name: 'StatusApi',
  data () {
    return {
      status: {},
      error: null
    }
  },
  created () {
    axios.get('api/status')
      .then((response) => {
        this.status = response.data
      })
      .catch((e) => {
        this.error = e.message
      })
  },
  methods: {
    tsToDate (ts) {
      return moment(ts * 1000).format('YYYY-MM-DD HH:mm:ss')
    }
  }
}
</script>
