---
title: "Solana GIF Dapp"
date: 2022-10-10T15:01:17+02:00
draft: false
featured_image: '/images/post_banners/solana.png'
math: true
tags: ["blockchain"]
summary: "I created a simple DApp running on Solana via the buildspace.so course.

Is a collaborative GIF image board, where users can authenticate via their Solana wallet.
The Solana blockchain is used as a database. The app is hosted decentralized on IPFS and ICP.
"
---

{{< fancybuttons 
    github="https://github.com/scheuclu/gif-portal-starter"
    deployed="https://pv5wp-eyaaa-aaaad-qeena-cai.ic0.app"
>}}

<!-- {{% fancybuttons %}} -->

After having done multiple Ethereum projects, I wanted to learn something new. I decided to give Solana a try.

# The App

This is a simple GIF dashboard. The [Solana blockchain](www.solana.com) is used as a database, keeping track of user submissions.
Users authenticate via a Solana web3 wallet, preferrably Phantom wallet, and can then collaboratively submit new GIFs.

![](https://github.com/scheuclu/gif-portal-starter/blob/main/gif-portal.gif?raw=true)

## Whats special about it?

Implementing this in web3 brings some special features.

1. There is no database. GIFs are stored directly on the Solana user accounts. The users pay for this with a small fee on GIF submission.
2. The frontend is hosted on Internet Computer and IPFS. This means that the webpage itself is hosted on a blockchain. There are no physical servers and no centralized app location. I was able to host this completely anonymously and with no cost to myself. It also cannot be censored by governments.

# About Solana
## Proof of History
Solana uses a combination of Proof of history and Proof of stake.
Proof of history allows to introduce the concept of time and temporal transaction ordering on a distributed ledger.
In essence, a function is repeatedly run over it's own output, typically a hash function. This leads to a naturally sequential, non-parallizable computation. Intermediate results of this loop are published, such that validator can check it in parallel.
The main idea is that it is guaranteed, that time has passed to create a block.
Read this [excellent post](https://github.com/lsmod/proof-of-history-explained) on how this helps to improve some aspects of Proof of Stake consensus.
## Scalability
Solana is capable of processing a very high number of transactions, exceeding even POS Ethereum.

## Decentralization
A relatively large stake of the original SOL allocation is owned by a small number of insiders, leading to potential issues with network improvisation and centralized control.

It is also relatively expensive to become a Solana Validator and break even.
Basically, validators earn money by collecting transactions fees as well as commission on the new tokens mined. The more SOL you have staked, the more often you become the current validator.
However, validators define their own commission rate. Currently, you can break even by staking around 700K USD in SOL and 0% commission rate. These validator will be favoured.

If you're interested in more details, I can recommend [this](https://medium.com/@Cogent_Crypto/how-to-become-a-validator-on-solana-9dc4288107b7) blog post.