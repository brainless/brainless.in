---
id: tag:blogger.com,1999:blog-27384460.post-7004580911712442727
title: "I uninstalled sqlite on my Linux box !!!"
date: 2007-04-04
author: brainless
categories: ['yum', 'server', 'apache', 'sqlite', 'linux']
---

Well I somehow felt I could yum erase sqlite since I do not need it. Well I did not see the dependencies that would be removed too! The result:

yum, rpm, php, httpd, rpm-python and many related packages all Erased !!! OMG I said. :P

I am not very friendly with Linux as yet at this level. I knew I had screwed all hopes of getting that box in clean shape. I searched the net for "reinstll RPM", "install RPM" and similar. Got a link to [How to reinstall rpm](http://www.redhat.com/archives/valhalla-list/2003-December/msg00020.html)

In case you can not reach to it, it says something like:

> 
> I guess you could try :  
> 
> - Copying the "rpm2cpio" binary from another machine  
> 
> - Copying the rpm package locally  
> 
> - Running something like :  
> 
>  cd /  
> 
>  rpm2cpio /path/to/rpm-4.\*.rpm | cpio -dimv  
> 
>   
> 
> Then you could clean up what you just did (in case it's a different version
> of rpm, mainly) :  
> 
> rpm -e --justdb --nodeps rpm  
> 
> rpm -Uvh /path/to/rpm-4.\*.rpm  
> 
>   
> 
> YMMV...  
> 
> Matthias  
> 
> 

That gave me some hope. I followed the instructions. Switched to root user, went to / and executed rpm2cpio with the downloaded rpm of RPM itself.
[RPM](ftp://ftp.rpm.org/pub/rpm/dist/rpm-4.2.x/)

Then got an error about librpm shared lib missing. So downloaded [librpm](ftp://ftp.rpm.org/pub/rpm/dist/librpm404/). Now rpm works!!!

Now I just searched for the latest versions of rpms for getting yum up and running. This included sqlite, python-sqlite, rpm-python, yum-metadata-parser, urlgrabber, etc. And finally installed yum !!!

I mainly used [rpm.pbone.net](http://rpm.pbone.net/) for searching rpms

Well thats it: I am almost saved :D