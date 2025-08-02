---
id: tag:blogger.com,1999:blog-27384460.post-116664946297517020
title: "Upgrading forum with phpBB2 and restoring from database backup"
pubDate: 2006-12-20
author: Sumit Datta
categories: ['php', 'open source', 'phpbb', 'hispanito']
---

Well I had to do some phpBB (phpBB2) issues for a client who runs [hispanito.com](http://hispanito.com/). He had a forum which ran on probably phpBB2 version 2.0.7 and with MySQL 4.x. Now I had to bring those data to a different server with MySQL 5.x

I tried a fresh install with latest phpBB2 version 2.0.21, but it failed as soon as I tried to bring in the old data. I tried an Upgrade too, but that failed too. Then I tried many other ways, none of which worked so at last I simply understood that table structures must have changed other than an very visible change in the number of tables ("session\_keys" was a new table). Now I had to edit the tables that had changed almost by hand, so if you must have to do the same here are the tables which I changed:

"users": two columns added: "user\_login\_tries" and "user\_last\_login\_try"

"sessions": one column added: "session\_admin"

"search\_results": one column added: "search\_time"

You have to do the above changes after you make a normal install of new phpBB2 and then restore old database backup, which will change the table structures.

Hope that helps.