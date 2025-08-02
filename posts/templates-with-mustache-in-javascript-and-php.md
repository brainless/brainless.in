---
id: tag:blogger.com,1999:blog-27384460.post-5653214013060187062
title: "Templates with Mustache in JavaScript and PHP"
date: 2011-02-15
author: brainless
categories: ['php', 'javascript', 'programming', 'mustache']
---

For a long time I have used PHP as the template language with nothing else on top of it. No template engines ever. This was all fine till the point that we wanted a **full AJAX UI** in [forums.com](http://forums.com) and also support basic view in non JavaScript mode. We also wanted to also change to a template structure which is more graphic designer or HTML developer friendly where only knowledge of HTML/CSS is needed. Thus we needed a **logic-less** no-frills template engine which has **support in JavaScript and PHP** at the minimum.

After searching a little we came across [**Mustache**](http://mustache.github.com), a logic-less template engine with support in many more languages than we needed. But we were certainly happy to see support in Python and Scala, just in case... Well a brief look at the readme in [JavaScript](https://github.com/janl/mustache.js) version and [PHP](https://github.com/janl/mustache.js) version will tell you the story: it is damn simple.

Mustache supports **Number, String, Array or Object** like data structures as its data source (view). It can also check for **Boolean and function returns**. Well that is more than sufficient for our needs. The major benefit was not that though. If you continue using any PHP based template system which you may end up having some PHP logic stuff somewhere in your templates after a while. This happened to us and we hated it. Our design team obviously wants to keep templates to themselves and thus the need to move to very clean templates.

Now how do we deal with **PHP and JavaScript versions**? We make one file per module in our system. So say discuss.html for templates related to discuss (Gab) system. Similarly user.html and usermanage.html and so on. Each file contains multiple individual templates which correspond to the sub-feature being requested. These are separated by HTML comments. The files are read in by a PHP code and provided as PHP array of strings to the PHP rendering engine or as JSON array of strings to the JavaScript rendering engine. This rendering engine is not Mustache, its a layer on top of it, which collects templates and data (view in Mustache language) and then send them for rendering.

The major difference between the PHP and JavaScript version of rendering is the way the layout is built. In the case of **PHP**, every sub-template is parsed, every inch of data prepared and then actual Mustache rendering starts. All this is **synchronous**. Smaller parts are fed to larger ones as strings, and so on. So we use **View Partials** in Mustache. But in the case of **JavaScript** rendering it is a different world. We only render outer portions first. For partials we render them later and **modify DOM** to insert them back to the page once the partials are rendered. So this allows us to have partials request their own data in **totally asynchronous** manner which is what we wanted.

We are still in process of developing this whole system. Of course we threw away hundreds of lines of old code to put this new system in place. And much of utility has shifted to JavaScript mode only. Also the back-end now behaves more like an API which just server JSON/PHP arrays.