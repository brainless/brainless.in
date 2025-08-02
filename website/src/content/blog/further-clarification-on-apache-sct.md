---
id: tag:blogger.com,1999:blog-27384460.post-114663951792888360
title: "Further Clarification on Apache SCT"
pubDate: 2006-05-04
author: Sumit Datta
---

Further Clarification on Apache SCT (Simple Config Tool)  

With regard to discussions on #httpd-dev channel on freenode yesterday I am posting some more details:
* The tool is not supposed to be a \*get everything done\* thingy. It will simply not read everything from your mind and do all settings.
* The main aim is to make it easier to understand the details and be a helper in self-study of the Apache config system, mainly the directives.
* The tool will simply not write anything to the filesystem (easlier I had thought of keeping this as an option) because of security reasons.
* The user can download a copy of generated .htaccess and place the file him/her-self on the filesystem.

Updates :  

May 4th 2:06 IST:  

* Internally the tool must store temporary data (or directives) in some temporary files etc. So that the tool can remember some settings the user had made previously and can revert back to it when needed. This will tremendously help a person to make experiments with the directives and learn.
* The tool can be made as a mod like mod\_asct (Apache Simple Config Tool). Since after we discussed on #httpd-dev, I intend not to put any write capabilities and only enable the download-and-copy-paste system so I guess if users want it then they can use a mod. This will be more helpful to admins of multi sites.