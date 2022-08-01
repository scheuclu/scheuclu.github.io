---
title: "Mandelbrot images"
date: 2022-06-14T15:01:17+02:00
draft: false
featured_image: '/images/mandelbrot.png'
katex: true
tags: ["math", "Python"]
---
<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

[Github](https://github.com/scheuclu/mandelbrot)&nbsp;&nbsp;
[Deployed](https://share.streamlit.io/scheuclu/mandelbrot_python/main/webpage.py)

# The Mandelbrot Explorer

## Overview
The goal of this project was to implement an interactive explorer for the [mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set).

It's definition is very simple. A complex number `c` is considered to be in the mandelbrot set if the iteration

$$\forall c \in \mathbb{C}: \\\\ ~ \\\\ z_{0}=0 \\\\ z_{i+1}=z_{i}^2+c$$


converges to a stationary value. Coloring all the convergent points, gives a picture like this

![](/images/mandelbrot_bw.png)

If instead, the above equation diverges, we can color that point based on how fast it diverges. This will create marvelous and complex fractal images like the one above.

![](/images/mandelbrot_480p.png)


The deployed website above let's you interactively inspect the set. I also created an animation of a zoom, deep into the set. I reccommend watching it in 4K :sunglasses:


{{< youtube 6KapQf8ZErs >}}

## Implementation
I had first implement the logic in [C++](https://github.com/scheuclu/mandelbrot).
However, I found it difficult to parrallelize this efficiently. What I could do is divide the area into `N` sub-areas, where `N` is the number of threads available. However, depending on where in the number plane one is, the iteration can take longer or it may abort sooner.

So, I could just create a huge heap with the pixels to be processed and then feed them to the compute threads 1 by 1.
However, I found that using `numpy.arrays` in Python is a lot more efficient.
This has the added benefit of IO becoming trivial.

You can find the implementation [here](https://github.com/scheuclu/mandelbrot_python).
