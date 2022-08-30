[TOC]

# How it works
The site is developed in pure markdown.

Hugo is used to generate a website.
For convenience, hugo is run on commit via [.github/workflows/gh-pages.yml](.github/workflows/gh-pages.yml).

The workflow runs automatically on commit and pushes the results to the branched named `gh-pages`.
I have configured the Github project to serve this branch.


See https://gohugo.io/getting-started/quick-start.


## Add a new post
```
hugo new posts/my-first-post.md
```


# Development
## Serve the site locally
```bash
hugo server -D
```

# Deployment

The site is deployed on netlify
[![Netlify Deploy Status](https://api.netlify.com/api/v1/badges/ebb8f08b-5796-4ed7-b016-e23dcd8ed5d7/deploy-status)](https://app.netlify.com/sites/inspiring-chebakia-744b5a/deploys)

