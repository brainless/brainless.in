---
id: tag:blogger.com,1999:blog-27384460.post-115777450494399864
title: "Apache 2.2 on Fedora Core 5"
pubDate: 2006-09-09
author: Sumit Datta
---

Me an some friends took a new server two days back. We threw in Xen and made four guests. I being in one of the guests which runs Fedora Core 5. I had to install Apache, which was pretty easy with yum. Just   

yum install httpd  

I started Apache using apachectl, and it seemed like all was OK, but I was not somehow able to view anything when I typed my server's IP in the browser from my home computer. Yet if I do a "telnet localhost 80" and "GET /" on the server itself ( I was logged in through SSH ), then I could view the HTML thrown at me by Apache.
After Googling about it I found that port 80 (http) might be blocked by default. I found some help and dropped the following line to /etc/sysconfig/iptables  

-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 80 ACCEPT  

Wow... I could see the default Fedora welcome page now.  

Now it was time to change my DocumentRoot to someplace else and also add Name based Virtual Hosts. When I changed my main DocumentRoot, Apache simply started throwing Forbidded errors. That was weird. It works with DocumentRoot set to /var/www/html but doesnt work when it is set to /srv/htdocs/   

Now I did chmod 0755 -R /srv/htdocs, but it didnt help. I again assumed someone else was to be blamed. So a second round of Googling and I found this:   

chcon -t httpd\_sys\_content\_t -R /srv/htdocs/  

That simply solved my problem again.  

(Note: you might need to repeat the above command for you logs and cgi-bin folders, if they are not the default ones).  

So it was an SELinux issue this time. Now most of my Apache 2.2 / Fedora Core 5 issues are fixed. Yay!!!