<template>
  <div id="bar">
    {{ info }}
  </div>
</template>

<script>
import { getAPI2 } from "@/axios";
export default {
  name: 'bar',
  data() {
    return {
      info: null
    };
  },
  mounted() {
    getAPI2
      .get()
      .then((response) => (this.info = response));
  },
};
</script>

<style>
</style>
