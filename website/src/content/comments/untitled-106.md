---
id: tag:blogger.com,1999:blog-27384460.post-6050952386163722523
title: "Untitled"
pubDate: 2011-12-29
author: Jes K
parent_id: tag:blogger.com,1999:blog-27384460.post-5430582065668541030
---

regarding UTF8 characters use mysql\_set\_charset('utf8','link');

eg.

$link = mysql\_connect($mysql\_server, $mysql\_username, $mysql\_password);
mysql\_select\_db($database,$link);
mysql\_set\_charset('utf8',$link);