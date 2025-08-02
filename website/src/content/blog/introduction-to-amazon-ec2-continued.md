---
id: tag:blogger.com,1999:blog-27384460.post-6037936862430515647
title: "Introduction to Amazon EC2 (Continued...)"
pubDate: 2009-05-14
author: Sumit Datta
categories: ['amazon', 'ec2', 'elasticfox']
---

Continued from [Introduction to Amazon Elastic Compute Cloud (Amazon EC2)](/2009/05/introduction-to-amazon-elastic-compute.html)...
So now that you have seen the feature lists and have some idea, lets start with the actual process. I will intentionally avoid going through details like EC2 Instance Types, Data Center Availabilities. These are relatively simple issues we can ignore now. We will come back to them maybe later. I will take you through a part by part tutorial of setting up a simple Drupal website on a fresh EC2 small instance. We will also setup WordPress on the same setup. We will deal with the full LAMP stack and our CMS apps including:

* Setting up a base [Gentoo](http://www.gentoo.org/) machine. Will do a [Debian](http://www.debian.org/) later.
* Installing the apps needed using [emerge](http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2&chap=1) on Gentoo and [apt-get](http://www.debian.org/doc/manuals/apt-howto/) on Debian
* Configuring [nginx](http://nginx.net/) (Will probably do [Apache](http://httpd.apache.org/) at a later time
* [PHP](http://www.php.net/) using php-cgi, [MySQL](http://dev.mysql.com/) server
* Setting up [Drupal](http://drupal.org/)
* Setting up [WordPress](http://wordpress.org/)

We will need a simple set of tools to do all this. If you are on Linux or similar you will not need an SSH client. On Windows you can get [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) or [Bitvise Tunnelier](http://www.bitvise.com/tunnelier). On Linux or Windows you will need [Elastic Fox](http://developer.amazonwebservices.com/connect/entry.jspa?externalID=609), which is an extension for [Firefox](http://www.mozilla.com/en-US/firefox) web browser and helps manage EC2 and related stuff. And before you start you will need an Amazon account. You will need a Credit Card but do not worry, you will be paying only for the stuff you need. So if the installation takes 1 hour on a small EC2 then you are going to [pay](http://aws.amazon.com/ec2/#pricing) $0.10 for the server and about similar amount for the data transfer. Pretty cheap right? Heh, you could send me a donation if you want to though :P

So start with getting an account from [Amazon WS](https://aws-portal.amazon.com/gp/aws/developer/registration/index.html), getting Firefox (if you do not already have it), install Elasticfox, set up the Amazon Access Key and Secret (you will get both of these under Your Account > [Access Identifiers](http://aws-portal.amazon.com/gp/aws/developer/account/index.html?action=access-key) in the top navigation menu).

Now before I jump into action (and Amazon starts billing you), let me explain in plain English what I want to do. Also I am clubbing the tasks up so that I can write them over a few blog posts, taking 2-3 days time. The first time I will do Gentoo/nginx/Drupal. We will come to Debian, Apache, WordPress combo later.

1. Create an SSH key-pair (from within Elasticfox). Create a small EC2 Instance from an existing AMI of Gentoo (using Elasticfox). Set simple Firewall stuff (using Elasticfox). [Continue here](/2009/05/basic-gentoo-on-amazon-ec2.html)...
2. Login to the Instance (server) using the Public Domain name we see in Elasticfox (which is of course given by Amazon). Install any extra software we need using "emerge".
3. Setup php-cgi in nginx. Get Drupal, setup nginx configuration for Drupal including rewrite rules (convert from the Apache rules supplied). Done!