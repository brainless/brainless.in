---
id: tag:blogger.com,1999:blog-27384460.post-4007791347865324566
title: "JavaScript to display meta content on the fly"
date: 2010-05-14
author: brainless
categories: ['json', 'javascript', 'jquery']
---

At forums.com we are trying to look at something similar to what Facebook and other sites do when it comes to displaying external content.  

Users usually refer to many kinds of URLs when they submit any content. From links to Wikipedia to Flickr, YouTube to WordPress. Each link can be either shown as a simple a tag (or video embed for video), or can be shown in a summary box with meta data from the external website.  

The process to do this is to take the user's data, find URLs, fetch the necessary sites, gather a summary and display it on forums.com instead of a simple a tag. I will not go into the details for fetching data from the external website, not today at least. But as we were discussing how to store and show this external information we found a nice way to do it.  

First of all, our background fetching, parsing was to be done mostly in Python, while the data may later be needed by any other code (PHP, Python, etc.). Thus it needed us to store this data in a format other than HTML tags inside the posts (which would be the easy way to get this done). For example a link to a Flickr image would get converted to a div with a title (a tag) and the image thumbnail (img tag). This is of course what the final output needed, but converting to HTML meant we would lose the data that we parse.  

But at the same time we do not want to store this extra data per post (rather per link and so on) in separate data stores. So it came to our minds, what if we simply store JSON strings in hidden spans inside the content. Later on, JavaScript can take the JSONs and convert to whatever HTML structure we may need.  

This solves two issues. First, our posts still stay more plain text (less HTML tags). Second, we still have our parse meta data in a data format. Plus the advantage: the JavaScript can be changed later to fit the future HTML structure needs for the site. Even better: different forums can switch on/off such stuff, or tweak the display as needed (of course we need to support such functionality, but we just might!).  

How to do it: Use span with a class (say json) and style="display:none;"  

Example JSON in the span:  

 `({"url":"http://discuss.lforums.com/asset/image/logo.png","title":"Forums"})`  

In jQuery do:  

`$('span.json').each(function(index) {  

 var data = $(this).html();  

 eval('data = ' + data);  

 $(this).replaceWith('![](' + data.url + ' "' + data.title + '")');  

})`  

We are still looking into this method, but seems it will suite our needs.

Please share your comments or suggestions.