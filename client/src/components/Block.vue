<template>
  <v-data-table :headers="headers" :items="desserts" class="elevation-1 mt-2" hide-actions="true">
    <template slot="items" slot-scope="props">
      <td>{{ props.item.name }}</td>
      <td class="text-xs-right">{{ props.item.value }}</td>
    </template>
  </v-data-table>
</template>

<script>
import moment from "moment";
export default {
  name: "Block",
  props: ["id", "previousHash", "proof", "transactions", "timestamp"],
  data() {
    return {
      headers: [
        {
          text: "Block ID",
          align: "left",
          sortable: false
        },
        {
          text: this.id,
          align: "right",
          sortable: false
        }
      ],
      desserts: [
        {
          name: "Timestamp",
          value: moment.unix(this.timestamp).format("YYYY-MM-DD HH:mm:ss")
        },
        {
          name: "Previous Hash",
          value: this.previousHash
        },
        {
          name: "Proof",
          value: this.proof
        },
        {
          name: "Transactions",
          value: this.transactions
            .map(
              transaction =>
                `${transaction.sender} sends ${transaction.amount} to ${
                  transaction.recipient
                }`
            )
            .slice(0, this.transactions.length - 1)
            .join(", ")
        }
      ]
    };
  }
};
</script>

<style>
</style>
