---
id: tag:blogger.com,1999:blog-27384460.post-5416775733766162506
title: "My laptop: my local web server"
date: 2007-03-08
author: brainless
categories: ['compaq', 'fedora core', 'apache', 'web', 'php', 'laptop']
---

Well two months back I bought my first laptop. A Compaq V3155AU with following configuration:  

AMD Turion64 (single core) 2.0Ghz  

Hyper Threading support  

512MB DDR2 system memory (I upgraded that to 1GB)  

nVidia 6150 graphics chip-set with shared memory  

14.1" display  

60GB SATA hard disk drive  

DVD/CD R+RW  

Bluetooth  

Ethernet  

Wireless Lan  

At sub Rs. 40,000 (sub US$ 900) this was a great deal. I was using Fedora Core 6 (64bit edition) on it but was not using it much since I still love my desktop and do not have enough work to justify simultaneous usage of two computers. Recently my friend planned to join me on web development work and I thought this was a good time to use it regularly. So I had to first make sure the Wireless Lan worked since I Fedora had not done that automatically. I read:  

"[Compaq Presario V3000 with Ubuntu 6.06](http://starbase-12.blogspot.com/2006/09/compaq-presario-v3000-with-ubuntu-606.html)" and it helped a lot. Actually I got the Wireless Lan running in no time. It was very easy. If after a shutdown or restart you need to connect just use the usual commands (iwconfig, iwlist, dhclient to scan for network, connect, etc.).  

I setup up my usual structure for web projects. PHP was already there, so was Apache. A few needed PHP modules were added ([APC](http://pecl.php.net/package/apc), [MagickWand](http://www.magickwand.org/) for [ImageMagick](http://www.imagemagick.org/)) and I had a working local web server !!!  

Things are really that easy if you are using the right software :) and there is always Google to help you when need it.