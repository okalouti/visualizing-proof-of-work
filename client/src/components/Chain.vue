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
  props: ["chain"],
  components: {
    Block
  }
};
</script>

<style>
</style>
