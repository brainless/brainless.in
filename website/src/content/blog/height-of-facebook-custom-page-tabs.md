---
id: tag:blogger.com,1999:blog-27384460.post-1638319214757570980
title: "Height of Facebook custom Page Tabs"
pubDate: 2012-01-13
author: Sumit Datta
categories: ['page tabs', 'facebook']
---

This is a quick tip: I am currently working on a Facebook app. I have a demo for a custom Page Tab. But somehow the height was not setting properly. The canvas height setting in the Developer setting was to Fluid. I have no clue where was the setting for Page Tab. Anyway after a little search I found that the following code works:  

<br />
FB.Canvas.setSize({height: 1500});<br />

I placed it at the bottom of my Application's custom Page Tab, before the end body tag. The height value is according to your needs. I am yet to look how this would work with flexible height (determined after iframe renders). Will update that later, for today this will do.