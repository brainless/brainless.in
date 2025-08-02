---
id: tag:blogger.com,1999:blog-27384460.post-116137262806648675
title: "Use ssh for http ftp and so on"
date: 2006-10-20
author: brainless
---

My ISP has a little fault that I use to my advantage. The software that they use works kinda in the following way:  

Before I login to their network all my external connections are blocked. I can not do http, ftp, ssh or anything else related to external network. This is usual isn't it.  

Now I login to my ISP using my username and password and i am connected!!! I have http, ftp, ssh and anything else that I can expect normally. This again is all usual.  

Now starts the unusual part: Lets assume I have my browser open and a normal download is going on in Firefox. Also assume I have ssh and sftp running. Now I log out of my network. Usually what you should expect is that all my connections stop. But here is where my ISP software is a good one for me. All connections on port 80 are blocked as soon as I logout; but no other connection ( on ports other than 80 ) that was open when I was logged in, is blocked. So ssh and sftp remain working. Similarly if i had torrent running it would continue to run. I never really made a test as to which ports are blocked and which are not, but at least I know many ports are not blocked.
Now the even more shocking part. My connection comes with unlimited data transfer, but is very limited in speed : 64 kbps. What happens after I logout is that the connections that were running ( non port 80 ones ) take as much bandwidth as available on the network!!!  

All I had to do was to somehow redirect all of my usual port 80 connections to some other port so that I could surf at a better speed or download the 2 Debian DVDs :) So I did some Google-ing for a solution. Somehow I thought that I could open an ssh to an external server I have and redirect all http, ftp through it. So this is what I got :  

use this command> **ssh -qTfnN2 -D 8080 user@server**  

This basically will connect to a server and open a local port 8080 so that now I could setup SOCKS proxy in Firefox through localhost:8080... and it works!!!  

Also I can download stuff using Curl through the above proxy too:  

use this command> **curl http://url/to/file --socks5 localhost:8080**  

And that works too.
Hope this helps you too :)