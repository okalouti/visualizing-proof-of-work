<template>
  <v-container>
    <v-layout row>
      <v-flex column xs12>
        <newTransaction/>
        <PendingTransaction/>
      </v-flex>
      <v-flex xs12>
        <chain/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import NewTransaction from "./components/newTransaction.vue";
import Chain from "./components/Chain.vue";
import PendingTransaction from "./components/PendingTransaction.vue";

export default {
  name: "App",
  components: {
    NewTransaction,
    PendingTransaction,
    Chain
  }
};
</script>

<style>
</style>
