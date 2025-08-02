---
id: tag:blogger.com,1999:blog-27384460.post-2629169169077756758
title: "Serve static files from nginx for POST request"
pubDate: 2012-01-13
author: Sumit Datta
categories: ['nginx', 'facebook']
---

This is a quick tip, I haven't had the time to dig deep into this. I am working on a Facebook app, and was doing a demo with static HTML. Everything was set, including SSL (I will write quick tip on that too). I could browse to the page separately. But it failed from within Facebook, giving a 405 error.  

From previous experience I remembered Facebook does POST requests, but I had forgotten the fix for static files. For some reason nginx does not allow serving static files for HTTP POST request. Anyway the fix was:  

    error\_page 405 = $uri;  

Also here is another suggestion: [Serving Static Content Via POST From Nginx](http://invalidlogic.com/2011/04/12/serving-static-content-via-post-from-nginx/)  

Hope this helps you.