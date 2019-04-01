<template>
  <v-form>
    <v-container>
      <v-layout column wrap>
        <v-flex xs12 sm6>
          <v-text-field v-model="sender" label="Sender" clearable></v-text-field>
        </v-flex>
        <v-flex xs12 sm6>
          <v-text-field v-model="receiver" label="Receiver" clearable></v-text-field>
        </v-flex>
        <v-flex xs12 sm6>
          <v-text-field v-model="amount" label="Amount" clearable></v-text-field>
        </v-flex>
        <v-btn
          depressed
          large
          class="white--text"
          color="blue accent-3"
          @click="submit(sender, receiver, amount)"
        >Submit</v-btn>
        <v-btn depressed large class="white--text" color="red" @click="mine">Mine</v-btn>
      </v-layout>
    </v-container>
  </v-form>
</template>

<script>
import axios from "axios";
export default {
  name: "New Transaction",
  methods: {
    mine() {
      this.toggleLoading();
      fetch("/mine")
        .then(() => {
          this.updateChain();
          this.updatePendingTransactions();
        })
        .then(() => this.toggleLoading());
    },
    submit(sender, receiver, amount) {
      return axios
        .post("/transactions/new", {
          amount: amount,
          sender: sender,
          recipient: receiver
        })
        .then(() => {
          this.updatePendingTransactions();
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    toggleLoading() {
      this.$emit("toggle-loading");
    },
    updateChain() {
      this.$emit("update-chain");
    },
    updatePendingTransactions() {
      this.$emit("update-pending");
    }
  }
};
</script>

<style>
</style>
