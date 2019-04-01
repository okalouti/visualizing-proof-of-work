# OVERVIEW

Proof-of-work is a consensus algorithm underpinning blockchain platforms such as Bitcoin and Ethereum.

For a through explanation of how it works and a wider dive into the nuts and bolts of a blockchain, please check out this [link](https://blog.goodaudience.com/blockchain-for-beginners-what-is-blockchain-519db8c6677a).

In the meantime, this is a simple interface to visualize how it works. Follow the steps below to simulate how it works:

- Enter transactions - i.e. _John sends 1 to Mary_ - and submit. Any transactions entered will be mined in the next block.
- Click on "Mine".

At this point, the algorithm takes an object representing the block to be mined - consisting of:

- A block ID that increments from the previous block
- The (cryptographic hash)[https://en.wikipedia.org/wiki/Cryptographic_hash_function] of the previous block.
- The transactions that are pending.

It will then start the process of finding a _proof_ (often referred to as a _nonce_) to add to this object, such that the hash of this object starts with four zeros. Once this proof is found, the new _block_ is added to the chain. The validity of the proof (once it is available) is easily verifiable.

Having a reference to the previous block ensures that each block is "chained" to the previous one. Imposing a requirement for the cryptographic hash means that it would require considerable computing power to alter a transaction, as one would then need to find a valid hash for all subsequent blocks in order to keep the integrity of the chain.

## SETUP

Install dependencies

```
cd client
yarn install
```

Run a build:

```
yarn build
```

Start the server:

```
cd ..
flask run
```

The interface should now be visible on localhost:5000.

## ARCHITECTURE

On the server side, the proof-of-work algorithm is written in _Python_ and the server is set up using _Flask_.

<p align="center">
<img  alt="Architecture" src ="./assets/python.png" width="100" margin-right ="40" hspace="20">
<img  alt="Architecture" src ="./assets/flask.svg" width="100" margin-left="40" hspace="20">
</p>

The front end is developed with Vue and Vuetify.

<p align="center">
<img  alt="Architecture" src ="./assets/vue.png" width="100" margin-right ="40" hspace = "20">
<img  alt="Architecture" src ="./assets/vuetify.png" width="100" margin-left="40" hspace = "20">
</p>

This project was undertaken in my time as a student at Code Chrysalis.
