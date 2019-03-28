<template>
  <div class="table">
    <v-data-table :headers="headers" :items="items" class="elevation-1 mt-2" hide-actions="true">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.sender }}</td>
        <td>{{ props.item.recipient }}</td>
        <td>{{ props.item.amount }}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PendingTransaction",
  props: ["sender", "recipient", "amount"],
  data() {
    return {
      currentTransactions: [],
      headers: [
        {
          text: "Sender",
          align: "left",
          sortable: false
        },
        {
          text: "Recipient",
          value: "recipient",
          sortable: false
        },
        {
          text: "Amount",
          value: "amount",
          sortable: false
        }
      ],
      items: []
    };
  },
  mounted() {
    axios.get("/transactions").then(response => {
      console.log(response);
      this.items = response.data;
    });
  }
};
</script>

<style scoped>
.table {
  max-width: 94%;
  margin-left: 16px;
}
</style>
