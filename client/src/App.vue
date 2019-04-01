<template>
  <v-container>
    <v-layout row>
      <v-flex column xs12>
        <newTransaction
          v-on:update-pending="updatePendingTransactions"
          v-on:update-chain="updateChain"
        />
        <PendingTransaction :pendingTransactions="pendingTransactions"/>
        <iframe
          src="https://giphy.com/embed/IwSG1QKOwDjQk"
          width="480"
          height="480"
          frameborder="0"
          class="giphy-embed"
          allowfullscreen
        ></iframe>
      </v-flex>
      <v-flex xs12>
        <chain :chain="chain"/>
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
    pendingTransactions: [],
    chain: []
  }),
  methods: {
    updatePendingTransactions() {
      axios.get("/transactions").then(response => {
        this.pendingTransactions = response.data;
      });
    },
    updateChain() {
      console.log("App component");
      fetch("/chain")
        .then(response => {
          return response.json();
        })
        .then(response => {
          this.chain = response["chain"];
        })
        .catch(err => console.log(err));
    }
  },
  mounted() {
    this.updatePendingTransactions();
    this.updateChain();
  }
};
</script>

<style>
</style>
