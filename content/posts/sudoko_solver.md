---
title: "Sudoku Solver"
date: 2022-04-02T15:01:17+02:00
show_reading_time: true
draft: false
featured_image: '/images/post_banners/sudoku.png'
katex: true

tags: ["machine learning", "Python"]
summary: "You can use the Sudoku Solver whenever you are stuck on a puzzle.  \n

It can read a playing field either directly via webcam or by uploading a picture and quicklu provide you with the solution.
"
---

{{< fancybuttons 
    github="https://github.com/scheuclu/sudoku_solver"
    deployed="https://share.streamlit.io/scheuclu/sudoku_solver/main/webpage.py"
>}}

You can use the Sudoku Solver whenever you are stuck on a puzzle.

I support both manual input as well as input via camera or webcam.

**Note** At the moment, the camera input is buggy, so you probably have to correct the results manually.

Here's a little demo of how it works.

{{< youtube swQfVmZG-00 >}}

## Overview
The solver consists of the following steps:

1. Read the image from webcam
2. Identify the Sudoku grid using classical computer vision
3. Dewarp the grid to rectangular format
4. Split the rectangle into 9x9 subimages
5. Identify the content of each subimage
6. Brute Force a solution

