---
id: tag:blogger.com,1999:blog-27384460.post-114684565620940642
title: "GData module for Drupal"
date: 2006-05-05
author: brainless
---

Introduction :  

[GData](http://code.google.com/apis/gdata/overview.html) is a
(new) [protocol](http://code.google.com/apis/gdata/protocol.html)
from Google which is based on RSS and Atom and combines both of them. Infact
underlying GData are actually RSS and Atom protocols. GData makes available :  

request (syndication), query (for search), insert, update and delete.  

All these together make \*remote\* usage of a CMS much more a reality and since
Google is behind this, there is a good chance of this becoming the de-facto standard in future.  

A little deeper :  

GData allows for content to be syndicated as well as inserted, updated and deleted.
Most importantly a seperate specification for query. Nice! GData uses XML as
described in existing Atom and RSS specs for all these. Different features, btw,
are supposed to use different HTTP request methods as outlines below:  

|  |  |
| --- | --- |
| Feature | HTTP method |
| Request / Query | GET |
| Insert | POST |
| Update | PUT |
| Delete | DELETE |

Note: 
There are alternatives to HTTP PUT
and HTTP DELETE : clients can use headers
'X-HTTP-Method-Override: PUT' and 'X-HTTP-Method-Override: DELETE' for PUT and DELETE respectively.  

There is also the authentication part in GData which as Moshe pointed out in
[drupal.org](http://drupal.org/node/60490), is Google specific, and
moreover work on it is still in progress. So for now I have not much concentrated
there. I hope that area will get better soon.  

Inside Drupal :  

As far as I have studied, some problems which exist in relation to GData are:
* Handling HTTP PUT and DELETE. PUT and
DELETE do not seem to work well on all servers and clients across platforms.
The headers ( X-HTTP-Method-Override: PUT and X-HTTP-Method-Override: DELETE )
ofcourse come to the rescue and to me the headers seem to be the best solution.
* Queries have to use the URL format: site.com/myFeed?
q=query-string Here, as again Moshe
pointed out on [drupal.org](http://drupal.org/node/60490) we, can
not use the q part. In discussion with
praseodym on
#drupal-soc, the best solution seems
to create a seperate file named say gfeed.php which handles user requests
and passes them onto drupal after doing modifications as necessary. So for
all GData related stuff there will exist clients will use URL site.com/gfeed.php?q=query.
gfeed.php is also used for non-query purposes like normal requests, insert,
etc. gfeed.php ofcourse sends the request to drupal after modifications
to the incoming request as necessary. Other solutions like using .htaccess also exist.

What is needed in GData module and how it is done:  

The GData module needs to define an API through which any module can register itself to expose data.  

Since GData allows for Insert or Updates, modules need to specify the access permissions too.  

There will be a file (say gfeed.php) which will take in actual user requests since in query
we need "q=something" format in URL and "q" has special meaning inside Drupal.
Thus normal bootstrap will not work, which brings in the need for gfeed.php.
Users/clients access Drupal GData in URL format : site.com/gfeed. When they
need to query they do site.com/gfeed?q=something gfeed.php then turns the request
to Drupal after doing required changes.  

Inside actual module the response is built and sent back to the user as XML.  

Links :  

[GData overview](http://code.google.com/apis/gdata/overview.html)  

[GData protocol](http://code.google.com/apis/gdata/protocol.html)  

[Drupal page on GData module](http://drupal.org/node/60490)  

[Roadmap for GData module](http://brainlessphp.blogspot.com/2006/05/roadmap-for-gdata-module-work.html)  

[Me in a Drupal project](http://brainlessphp.blogspot.com/2006/05/me-in-drupal-project.html)  

Related Links Elsewhere on the GData buzz :  

[GData - Google's new syndication protocol](http://blogs.zdnet.com/web2explorer/?p=162) : From ZDNet.com  

[Google's GData, MySQL, and the Future of on-line Databases](http://jeremy.zawodny.com/blog/archives/006687.html) : Jeremy Zawodny's blog  

[Why Google is extending RSS](http://blogs.zdnet.com/web2explorer/?p=165) : From ZDNet.com  

[Google Data APIs Protocol](http://bitworking.org/news/Google_Data_APIs_Protocol) : Joe Gregorio  

[Google and RSS: GData](http://afeedisborn.com/google-and-rss-gdata/) : By Vincent  

[Google syndication](http://www.buzzmachine.com/index.php/2006/04/21/google-syndication/) : By Jeff Jarvis  

[GData - Google BCM protocol](http://blog.deeje.tv/musings/2006/04/gdata_google_bc.html) : By Deeje Cooley  

 [GData: The end of Google's walled garden](http://blog.mauricecodik.com/2006/04/gdata-end-of-googles-walled-garden.html) : By Maurice Codik  

[GData is a new protocol based on Atom 1.0 and RSS 2.0](http://www.paradox1x.org/weblog/kmartino/archives/004528.shtml) : By Karl Martino  

[GData is about more than Google Calendar integration](http://cse-mjmcl.cse.bris.ac.uk/blog/2006/04/21/1145613127721.html) : By Mark McLaren  

 [GData: Google's Extensible API](http://radioactiveyak.blogspot.com/2006/04/gdata-googles-extensible-api.html) : By Reto Meier  

[Google introduces GData: Google Calendar API](http://labnol.blogspot.com/2006/04/google-introduces-gdata-google.html) : By Amit Agarwal  

Also ASF has an application titled "[Implement a Google Data API (GData) server using Lucene](http://wiki.apache.org/general/SummerOfCode2006#lucene-gdata-server)"
for SoC 2006.