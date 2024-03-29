---
title: "Implementing a calculator from scratch"
date: 2022-05-29T15:01:17+02:00
show_reading_time: true
draft: false
featured_image: '/images/post_banners/numbers.png'
summary: "This project came out of an interview task I once had to complete.\n

The goals is to implement a fully working calculator, without using any of the standard libraries.\n

The calculator is able to accept arbitrary string that represent and expression or equation and solve it.\n
"
---

{{< fancybuttons 
    github="https://github.com/scheuclu/mandelbrot"
    deployed="https://share.streamlit.io/scheuclu/overkillcalculator/main/webpage.py"
>}}

The goal of this project was to implement a calculator from scratch.
Notably, I wanted to do it without the use of any sophisticated libraries.

Here's the feature specification:

 - Infix and Reverse Polish notation are supported.
 - Parentheses are supported.
 - Basic arithmatic as well as trigonometric functions are supported.
 - Supports basic constants such as Eulers number or Pi.
 - The calculator can solve for one unknown in a linear equation.
 - Proper error handling
 - Fully tested, of course.

The implementation can be found [here](https://github.com/scheuclu/OverkillCalculator).


![Demo](/images/calculator.gif)
