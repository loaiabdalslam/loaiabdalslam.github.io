Title: Using Github Issues for comments
Author: gozar
Date: 2018-11-24 16:47
Slug: using-github-issues-for-comments
Category: Software
Tags: github,comments
Status: published

For publishing this website, I use [Pelican](https://blog.getpelican.com), a static website generator. Publishing a static website has many advantages, such as no databases required and the ability to host for free on Github. The biggest downside is the lack of commenting on articles. A lot of static websites will use [Disqus](https://disqus.com), which works but then I'll have ads on my website. As I researched options, I came across [Utterances](https://utteranc.es).

# Storing comments in Github Issues

Comments are tricky because you need some sort of server in place somewhere to accept comments and a way to place them on the webpage. Utterances uses the Issues interface in Github to store the comments, and some Javascript on the webpage to show the comments or allow someone to comment. Unfortunately, this set up does require the commenter to have a Github account.

Once the Javascript is added to the posts, Utterances will show any comments to the current page, and will automatically create an issue for the current page if one doesn't exist.

I'll play with it and see how it goes.
