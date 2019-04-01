<template>
  <v-container>
    <v-layout row>
      <v-flex column xs12>
        <newTransaction
          v-on:update-pending="updatePendingTransactions"
          v-on:update-chain="updateChain"
          v-on:toggle-loading="toggleLoading"
        />
        <div v-if="loading" class="loading">
          <iframe
            src="https://giphy.com/embed/IwSG1QKOwDjQk"
            width="200"
            height="200"
            opacity="0.75"
            frameborder="0"
            class="giphy-embed"
            allowtransparency="true"
          ></iframe>
        </div>
        <PendingTransaction v-if="!loading" :pendingTransactions="pendingTransactions"/>
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
    chain: [],
    loading: false
  }),
  methods: {
    toggleLoading() {
      this.loading = !this.loading;
      console.log(this.loading);
    },
    updatePendingTransactions() {
      axios.get("/transactions").then(response => {
        this.pendingTransactions = response.data;
      });
    },
    updateChain() {
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
.loading {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
</style>
