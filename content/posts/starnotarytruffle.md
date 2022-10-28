---
title: "Solidity Star Notary DApp"
date: 2022-10-26T15:01:17+02:00
draft: false
featured_image: '/images/post_banners/stars.jpg'
math: true
tags: ["blockchain"]
summary: "A DApp built on Ethereum using truffle, hosted on the Goerli test chain.

I implemented an ERC721 token in Solidity representing Star name ownership. Anyone can connect, mint and trade stars.
"
---

{{< fancybuttons 
    github="https://github.com/scheuclu/SolidityStarNotary"
    deployed="https://dashing-gumdrop-fd8d06.netlify.app"
>}}



This was one of the projects implemented during my [Blockchain Developer Nanodegree](https://graduation.udacity.com/confirm/PRDLGCYP).

It implements the following
- **A smart contract**
  - The contract represent an NFT, based on ERC721, that is used to trade star ownership. I used [open-zeppelin](https://www.openzeppelin.com) for the ERC721 interface.
- **A fully covered set of tests.**
  - I used truffle and mocha for testing my smart contract. All tests can be found [here](TODO.
- **Deployment to the Goerli test chain**
  - I find the development workflow on Ethereum very excruciating compared to Solana. It has become painful to get your hands onto testnet tokens. And, even if you get some, deploying to the testnet is expensive. If you want to use my contract, you will need some Goerli I recommend [this faucet](https://goerli-faucet.pk910.de/).

## Demo
{{< youtube e_G52ygBv94 >}}

