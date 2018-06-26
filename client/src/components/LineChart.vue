<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: {
    label: {
      type: String,
      required: true
    },
    labels: {
      type: Array,
      required: true
    },
    points: {
      type: Array | Object,
      required: true
    }
  },
  data () {
    return {
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            },
            gridLines: {
              display: true
            }
          }],
          xAxes: [ {
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  mounted () {
    this.renderChart({
      labels: this.labels,
      datasets: [
        {
          label: this.label,
          data: this.points,
          backgroundColor: '#f879799e'
        }
      ]
    }, this.options)
  }
}

</script>
