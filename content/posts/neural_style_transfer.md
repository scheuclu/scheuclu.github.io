---
title: "Neural Style Transfer"
date: 2022-06-19T15:01:17+02:00
draft: false
featured_image: '/images/style_transfer/result/favourites/edritz_pop_art.jpg'
math: true
---

# Neural Style transfer

In this project, I implemented neural style transfer in PyTorch.

The goals is simple. We take a `content image` and a `style image`. The goal is to keep the semantic content of the `content` image, but draw it in the style of the `style image`.

To do this, we start with a simple classification Convolutional Neural Network (CNN). A CNN  encodes a high resolution image into a large number of low-resolution features channels. These channels encode common semantics of the training set.

![](/images/cnn.png)

See also [here]([TODO](https://en.wikipedia.org/wiki/Neural_style_transfer)) for a more extensive explanation.

In my case I used VGG-19. Now, VGG-19 takes an input image, succcesively applies convolutions until a much smaller feature map is obtained. The feature map is then fed into a softmax to obtain classifications for N classes.



## The style matrix
The style matrix is also called a "Gram matrix." In linear algebra, the Gram matrix G of a set of vectors $(v_{1},\dots ,v_{n})$ is the matrix of dot products, whose entries are $${\displaystyle G_{ij} = v_{i}^T v_{j} = np.dot(v_{i}, v_{j})  }$$. In other words, $G_{ij}$ compares how similar $v_i$ is to $v_j$: If they are highly similar, you would expect them to have a large dot product, and thus for $G_{ij}$ to be large. 



## Style cost
After generating the Style matrix (Gram matrix), your goal will be to minimize the distance between the Gram matrix of the "style" image S and that of the "generated" image G. For now, we are using only a single hidden layer $a^{[l]}$, and the corresponding style cost for this layer is defined as: 


$$ J_{style}^{[l]}(S,G) = \frac{1}{4} \times {n_C}^2 \times (n_H \times n_W)^2 \sum _{i=1}^{n_C}\sum_{j=1}^{n_C}(G^{(S)}_{ij} - G^{(G)}_{ij})^2 $$

where $G^{(S)}$ and $G^{(G)}$ are respectively the Gram matrices of the "style" image and the "generated" image, computed using the hidden layer activations for a particular hidden layer in the network.  


So far you have captured the style from only one layer. We'll get better results if we "merge" style costs from several different layers. After completing this exercise, feel free to come back and experiment with different weights to see how it changes the generated image $G$. But for now, this is a pretty reasonable default: 

You can combine the style costs for different layers as follows:
$$J_{style}(S,G) = \sum_{l} \lambda^{[l]} J^{[l]}_{style}(S,G)$$


Finally, let's create a cost function that minimizes both the style and the content cost. The formula is: 
$$J(G) = \alpha J_{content}(C,G) + \beta J_{style}(S,G)$$


{{< gallery  caption-effect="none" >}}
  {{< figure src="/images/style_transfer/content/edritz_content_image.jpg" caption="content" >}}
  {{< figure src="/images/style_transfer/style/pop_art.jpg" caption="style" >}}
  {{< figure src="/images/style_transfer/edritz/edritz_pop_art.jpg" caption="result" >}}

  {{< figure src="/images/style_transfer/content/edritz_content_image.jpg" caption="content" >}}
  {{< figure src="/images/style_transfer/style/wood.jpg" caption="style" >}}
  {{< figure src="/images/style_transfer/edritz/edritz_wood.jpg" caption="result" >}}

  {{< figure src="/images/style_transfer/content/edritz_content_image.jpg" caption="content" >}}
  {{< figure src="/images/style_transfer/style/mona_lisa.jpg" caption="style" >}}
  {{< figure src="/images/style_transfer/edritz/edritz_mona_lisa.jpg" caption="result" >}}

  {{< figure src="/images/style_transfer/content/edritz_content_image.jpg" caption="content" >}}
  {{< figure src="/images/style_transfer/style/lilies.jpg" caption="style" >}}
  {{< figure src="/images/style_transfer/edritz/edritz_lilies.jpg" caption="result" >}}
{{< /gallery >}} {{< load-photoswipe >}}