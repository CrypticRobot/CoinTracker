<template>
  <div class="collapse">
    <div class="collapse-trigger" @click="toggle">
      <slot name="trigger" :open="isOpen" />
    </div>
    <!-- must use `v-if`` rather than `v-show`` -->
    <!-- Difference between those please refer to https://vuejs.org/v2/guide/conditional.html#v-if-vs-v-show  -->
    <div class="collapse-content" v-if="isOpen">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Collapse',
  props: {
    open: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      isOpen: this.open
    }
  },
  watch: {
    open (value) {
      this.isOpen = value
    }
  },
  methods: {
    toggle () {
      this.isOpen = !this.isOpen
      this.$emit('update:open', this.isOpen)
      this.$emit(this.isOpen ? 'open' : 'close')
    }
  }
}
</script>
