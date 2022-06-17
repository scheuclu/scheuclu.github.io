---
title: "Sudoku Solver"
date: 2022-04-02T15:01:17+02:00
draft: false
featured_image: '/images/sudoku.png'
katex: true
---


[Github](https://github.com/scheuclu/sudoku_solver)&nbsp;&nbsp;
[Deployed](https://share.streamlit.io/scheuclu/sudoku_solver/main/webpage.py)

# Sudoku Solver

You can use the Sudoku Solver whenever you are stuck on a puzzle.

I support both manual input as well as input via camera or webcam.

**Note** At the moment, the camera input is buggy, so you probably have to correct the results manually.

Here's a little demo of how it works.

![](https://www.youtube.com/watch?v=swQfVmZG-00)

## Overview
The solver consists of the following step

1. Read the image from webcam
2. Identify the sudoku grid using classical computer vision
3. Dewarp the grid to rectangular format
4. Split the rectangle into 9x9 subimages
5. Identify the content of eacht subimage
6. Brute Force a solution

