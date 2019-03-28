<template>
  <v-container fluid>
    <Block
      v-for="block in chain"
      :key="block.index"
      :id="block.index"
      :previousHash="block.previous_hash"
      :proof="block.proof"
      :timestamp="block.timestamp"
      :transactions="block.transactions"
    />
  </v-container>
</template>
<script>
import Block from "./Block.vue";

export default {
  name: "Chain",
  data: () => ({
    chain: []
  }),
  components: {
    Block
  },
  // eslint-disable-next-line
  mounted() {
    fetch("/chain")
      .then(response => {
        return response.json();
      })
      .then(response => {
        this.chain = response["chain"];
      })
      .catch(err => console.log(err));
  }
};
</script>

<style>
</style>
