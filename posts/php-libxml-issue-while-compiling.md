---
id: tag:blogger.com,1999:blog-27384460.post-5691130889835970261
title: "PHP libxml issue while compiling"
date: 2012-02-28
author: brainless
categories: ['php', 'linux']
---

Today I had some trouble getting libxml to work in PHP. I was compiling PHP 5.3.10 for a client's Joomla site and it needs libxml. The issue seemed to be commonly happening to many people and I came across a number of forum threads on the topic.  

The suggestions mostly hover around installing libxml2 development package. This can be done in Debian or Ubuntu by:  

apt-get install libxml2 libxml2-dev  

On other Linux distributions you may try libxml2-devel  

But I had already done that and still libxml was not showing up in PHP. I had the --with-libxml-dir setting in ./configure with no luck.  

Then I came across the --enable-libxml setting, which although is not mentioned directly in the `./configure --help`, it should have come to my mind. This is how you enable (or disable with --disable) any module from the ext/ directory. Anyway, I found it mentioned [here](http://joomla.unlikelysource.com/index.php/misc-tutorials-category/22-howto-install-php53) and that worked! The reason for this is because I had --disable-all option set. So all default modules were off, and I had to enable libxml with its enable option.  

Hope this helps someone else...