
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