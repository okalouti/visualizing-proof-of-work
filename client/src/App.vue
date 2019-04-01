<template>
  <v-container>
    <v-layout row>
      <v-flex column xs12>
        <newTransaction v-on:update-pending="updatePendingTransactions"/>
        <PendingTransaction :pendingTransactions="pendingTransactions"/>
      </v-flex>
      <v-flex xs12>
        <chain/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";

import NewTransaction from "./components/newTransaction.vue";
import Chain from "./components/Chain.vue";
import PendingTransaction from "./components/PendingTransaction.vue";

export default {
  name: "App",
  components: {
    NewTransaction,
    PendingTransaction,
    Chain
  },
  data: () => ({
    pendingTransactions: []
  }),
  methods: {
    updatePendingTransactions() {
      axios.get("/transactions").then(response => {
        this.pendingTransactions = response.data;
      });
    }
  },
  mounted() {
    this.updatePendingTransactions();
  }
};
</script>

<style>
</style>
