---
id: tag:blogger.com,1999:blog-27384460.post-8921073563232310246
title: "Problems with installing Yum on Fedora Core 4"
date: 2007-03-07
author: brainless
categories: ['yum', 'fedora core', 'open source', 'python', 'rpm']
---

"There is a problem importing one of the Python modules" : ever faced this error after installing an running yum. Well I faced that. And searched on Google for it. But in vain. Most results suggested the usual missing packages:

```
libxml2-python, python-sqlite, or python-elementtree
```
I tried installing all of them and no use. Then did lot of finding around and finally i tried to install other package managers. Finally I cam across a yum rpm package at rpmfind.net and while installing I got the dependency error for urlgrabber (http://linux.duke.edu/projects/urlgrabber/).
Installed that and all was fine !!!