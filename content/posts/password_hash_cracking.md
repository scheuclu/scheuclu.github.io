---
title: "Password Hash Cracking"
date: 2022-07-27T15:01:17+02:00
show_reading_time: true
draft: false
featured_image: '/images/post_banners/password.webp'
plotly: true
math: true
custom_table: true
tags: ["cryptography", "hashing", "Python"]
summary: "I'm taking a look how user-authentifications works.  \n
We will dive a bit into hash functions  \n
Finally, we try to recover passwords from leaked hashes using GPUs.  \n
Addittionally, I'll provide some complexity considerations as well as cost estimations."
---
<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

[Github](https://github.com/scheuclu/hash_cracking)&nbsp;&nbsp;

{{< toc >}}

---
## Motivation
I recently had an unauthorized access on my Amazon account. Luckily, Amazon sent me a 2-factor authentification request to confirm my login, which I promptly denied, but it got me interested in how these kind of attacks work.  
Now, I have been using a password manager for years ([Bitwarden](https://bitwarden.com/)), but my Amazon account predates it and I guess, I was too lazy to change the password.

So, out of curiosity, I started investigating how these kinds of attacks work.


---
## How do online logins work?
In essence, a website has a database with of valid logins. When you enter your username and password, you provide one on these valid logins.  
However, these databases do not actually store your passwords because it would be incredibly unsafe for, if the website gets compromised and the database leaked, everyone would now know your password, which is probably being used on other pages too.

Instead, your username is stored alongside the hash of your password. If a leak occurs, only the hash is published. An attacker would still not know what password led to that hash.
### A quick intro to hash-functions
The fundamental technology behind safe logins to websites are hash-functions. A hash function has a few characteristics:
- **arbitrary length input**
- **non-injective, non-surjective:** Each input maps to a specific output. Different inputs may map to the same output. There may be points in the output space that have no corresponding input.
- **no correlation between inputs and outputs:** Given two points $x_1$ and $x_2$ in the input space which map to $y_1$ and $y_2$ in the output space, there should be no correlation between $||x_2-y_1||$ and $||y_2-y_1||$. In lay-mans terms, this means that if two points in the input space are simiar, if you run them through the hash funciton, they should give very diffrent outputs.
- **uniform output distribution:** All points in the output space should be approximately equally likely. This is another way of saying there should be as little collisions as possible.

### Let's design a trivial hash function

We are searching for a hash function that maps a number $N \in [0 ... 2^8]$ to a hash $h(N) \in [0 ... 2^8]$.

Naively, we can simply reverse the binary representation.

```python
def naive_hash(n):
  b=bin(n)
  b=b[2:].rjust(8, '0')
  h=int(b[-1::-1],2)
  return h
```

Now, we can take any arbirary `ASCII` string and compute it's hash by summing up the hashes of it's binary representations modulo `2^8`.

```Python
def dummy_hash_password(s):
    return sum([dummy_hash(ord(i)) for i in s]) % 2**8
```

| Password      | hash |
| :---        |    :----   |
| code      | 136       |
| code1      | 20      |
| code1!   | 152        |



At first glance, this looks like a good random hash:
{{< plotly json="/plots/input_to_output.json" height="400px" >}}

But there are still hidden patterns in the outputs as shown here:
{{< plotly json="/plots/pattern.json" height="400px" >}}

In practice, designing good hash funcitons in incredible difficult and still an active area of reasearch. Modern hash function are a complicated interwoven set of operations.

Also:

| Password      | hash |
| :---        |    ----:   |
| code      | 136       |
| Code      | 132      |
| bear   | 192        |
| Bear   | 188        |
| water   | 150        |
| Water   | 146        |

I hope you see the pattern. Even if we extended this hash function to a greater bit length, it would be incredibly unsafe.



What we have created above is an *8-bit hash function*, meaning that it's output space is 8-bits. The hashes are therefor numbers in the range of `[0 ... 255]`.

Modern hash functions are much larger than that. E.g. [SHA256](https://en.wikipedia.org/wiki/SHA-2) uses 256 bit, meaning that there are a total of `2^56`(`1.1579209e+77`) different outputs.
For comparison, the number of sand grains on earth is estimated at `7.5e18` grains and the number of atoms on earth at `1.33e50`.
So, if you created a new planet earth for every sand grain on earh, you would need `9.8e68` atoms, which is still a billion times less than there are outpout possibilities in `SHA-256`.


### How hashes are used to identify yourself online
When you login online, you typically provide a `username` and a `password`.
The server then checks whether this particular combination is known.
A bad practice, which is still encountered sometimes, would be for the server to simply store a table of `username`-`password` combinations.
However, there is always the possibility for a server to be compromised and the table to be leaked on the internet.
So, instead, websites typically store your username along with the hash of your password. When you log in, the server quickly computes the hash of the password you provided and compares it against the one it has stored.

If the table ever gets leaked, an attacker now has you password hash. But in order to get access to your account, he then needs to find a password that produces this exact hash. Typically this is done via brute-force attack.

---
## Brute-forcing password hashes

As discussed about, servers sometimes get compromised and login data is leaked. I guess this is what happened to me,
An attacker now has a username and a password hash. Let's assume the hash is in `SHA1` format.

Now, in a brute-force attack, an attacker simply tries to guess the password by trying all possible combinations of inputs until they find one that creates the leaked hash. If he finds one, the hacker can then log into the site using this input as password. Due to collissions, this might not even be the same password you've been using, although it is highly likely.


---
## Complexity considerations

Brute forcing the password from a hash seems straight forward. In reality however, this task very quickly becomes computationally infeasible, unless one is willing to spend an excuberant amount of computational resources.  

Let's look at some examples:

### A naive approach

To get an idea of how complex it is to recover the password from a hash, let's make a few assumptions:

1. Our hash is [SHA-1](https://en.wikipedia.org/wiki/SHA-1). This is a 128 bit hash.
1. The password only consists of upper and lower case letter as well as digits. This means we have an alphabet of `26*2+10=62` characters.
1. We use an RTX-3090 on vast.ai to recover hashes. It has a SHA-1 hashrate of 22757.6 MH/s.
1. We use the cheapest cloud provider I was able to find, at 0.31$ an hour for the RTX-3090.

this gives the following table:

| password length | # password options | time to bruteforce [min] | cost[^1] |
| ----------- | ----------- | --- | --- |
| 1 | 62 | 2 ns | free |
| 2 | 3.8e3 | 16 us | free |
| 3 | 2.3e5 | 104 ms | free |
| 4 | 1.4e7 | 6 ms | free |
| 5 | 9.1e8 | 40 ms | free |
| 6 | 5.6e10 | 2.5 s | free |
| 7 | 3.5e12 | 2.5 min | 1ct  |
| 8 | 2.1e14 | 2.6 h | 82 ct |
| 9 | 1.3e16 | 6.9 d | 51 $ |

Now, most of us have experienced that websites require us to use special symbols. Let's just consider the 5 most used ones: `["_", ".",  "-", "!", "@", "*", "$", "?", "&", "%"]`. We now have `72` different characters in our alpahabet.

This simple addition changes the table as follows:

| password length | # password options | time to bruteforce [min] | cost[^1] |
| ----------- | ----------- | --- | --- |
| 1 | 62 | 4 ns | free |
| 2 | 3.8e3 | 23 us | free |
| 3 | 2.3e5 | 164 uss | free |
| 4 | 1.4e7 | 11 ms | free |
| 5 | 9.1e8 | 850 ms | free |
| 6 | 5.6e10 | 6 s | free |
| 7 | 3.5e12 | 7.3 min | 4 ct |
| 8 | 2.1e14 | 9 h | 3 $ |
| 9 | 1.3e16 | 26 d | 200 $ |



### A statistically determined approach
As you can see, it very quicly becomes infeasible to crack this hash with increasing password length.

However, we can take advantage of human psychology. Here's some of the most commonly used observations
1. People often use capital letters at the beginning.
2. Special characters are most likely used at the very end.
3. Different characters have different likelihood. E.g. The most commonly used letter is `e` and the most commonly used special character is `-`.
4. Passwords are often variations of actual words/names. E.g. `Jacob  -> J4c0b!`. By using a dictionary and performing most common manipulations, we can quickly test for all of the variations.

While taking likelihoods into account does not change the total search space, it drastically reduces the average time until the password is found.

Let's have a look at the numbers with just 2 simple modifcations to the last table:
1. We assume that only the first symbol is a captial letter
2. We assume that the last symbol is a special character of number.

This results in the following table:


| password length | # password options | time to bruteforce [min] | cost[^1] |
| ----------- | ----------- | --- | --- |
| 4 | 1213056 | 90 us | free |
| 5 | 43670016 | 320 us | free |
| 6 | 1572120576 | 1 ms | free |
| 7 | 56596340736 | 40 ms | free |
| 8 | 2037468266496 | 1.5 s | free |
| 9 | 73348857593856 | 54 s | 28 ct |


As you can see, the cost is drastically reduced, while we will still recover a vast majoriy of passwords using these assumptions.


## A concrete example
With all of the above considerations in mind, let's have a look at some arbirarly though-up passwords:

| password | SHA1 hash |
| --- | --- |
| tabletop | dd702c884ce8179f443aca343d61175408396b4f |
| !Energy! | dd8a0212c9a8950ac116962cf2bf3b6746e95a79 |
| 21EXg4vI | 7a0fd2b60e88468a60db9d8812b0cfa2d1f25700 |

We use hashcat on a RTX-3090 to try and attach these hashes.  
As discuassed above, a pure bruteforce approach with all possible characters, quickly becomes infeasible.
An attacker will most likely try the simplest appraoches first, and then successively try more expensive configs, until success is achieved.
Pretending not to know the cleartext passwords, we will try the following modes:

| attack mode | descrition | # combos | worst case runtime | worst case cost |
| ---         | ---        | ---      | ---                | ---             |
| 1 | combination of lower-case letters | 2.1e11 | 9s | free |
| 2 | upper-, lower-case, numbers and 10 symbols | 7.2e14 | 9h | TODO |
| 3 | dictinary attack with simple modifications | TODO | TODO | TODO |

Using these attach modes one after the other, I was able to crackt the passwords in the following timespans:

| password | time to crack | cost |
| ---      | ---           | ---           |
| tabletop | 2 min | free |
| !Energy! | 26 h| 8 $ |
| 21EXg4vI | 3 h | 1 $ |

What is more, the problem can be perfectly parallelized in multiple GPUs, thus almost bringing down the solution time arbitrarily, without a significant increase in overall cost.

## Password attack using dictionaries

It has been shown that, non-tech savy users in particular, use password derived from real words. This could be names, cities or something similar which is then slightly modified to adhere to modern website password standards. E.g. "Beverly" could become "1Beverly!", "B3v3rly", or "?Beverly1!".
If the password follows this patterns, than cracking using dictionaries plus modifications can be extremly effective.

From our 3 example passwords above, 2 should be crackable like that. let's give it a try!\
First, we need to find a dictionary to use.

**[TBD]**









[^1]: Based on a RTX-3090 instance on [vast.ai](https://vast.ai).
[^2]: Practically zero cost involved.
