---
id: tag:blogger.com,1999:blog-27384460.post-5070612901163842360
title: "Dummies Introduction to Amazon Web Services"
date: 2009-05-13
author: brainless
categories: ['amazon', 's3', 'aws', 'ec2']
---

Lot of you may have heard of this. Well certainly you have heard of Amazon.com and if you are into software/IT/web there is a good chance someone in your company is thinking of that mumbo jambo called cloud computing. Well what the hell is all this and then this web services?

Note: most of what I do is related to running websites. So whatever I write here will also relate to that. Beyond that I don't know nothing :|

Cloud Computing
Well there is this thing called a computer. You know it right. And you know that you need them to run your websites or web apps or what else you call them. So what choices do you have? Well here are some:
1. you can take a shared hosting account
2. can take a dedicated server
3. you can take a hosted option to run your website
4. host the website from your own home/office
5. get virtual dedicated server (its like a small slice out of a server, each slice is independent of the other at the OS layer) (short: vds)
6. or you can take a cloud service

So you can assume the cloud service is maybe not radically different from the other options. I mean it still has to run your site or app. It just differs by the way you get the service, manage it, use it. Lets understand an example:

I need to host this blog.

I can take a shared hosting account which will allow me to run a site on a server that is being shared among many other users. Each user is running from his/her own folder. Each having maybe a few MySQL or similar database server users. Some hosts will allow to use a custom .htaccess file in your folder to use custom re-write rules etc. under Apache.

Now that seems a headache for a site which is just running a blog? Well take an account from WordPress.com or Blogger, LJ, etc. These are the hosted options.

I could also take a full dedicated server or a virtual server if I need, but I will to maintain it myself. Also getting a fully dedicated server setup takes sometime (1 day or more).
The last option is that I take a cloud service. What I get is an independent slice like in a virtual dedicated host. But its more. A basic cloud service should give me access to the service fast. So a new slice fitted with 1GB or RAM/X Ghz of processor etc. should be up in just a few minutes maybe. This is same in vds. The most important part: all the setup, settings should be available through APIs. What was that? Well I should have a simple protocol (mostly http based) which I or my custom code or some app can access to create a new slice, or get a bigger slice if available, check status, and maybe other stuff. That is the most important part. The ability for software itself to create its own environment to run on! Confused? Even I am :P ... well don't worry, I will explain.

Now there are many examples of cloud services, but I have (sadly) enough exposure in just one: Amazon Web Services. So lets dig into it.

Amazon Web Services

Main [website](http://aws.amazon.com/)

Services [listing](http://aws.amazon.com/products/):

[Amazon Elastic Compute Cloud (Amazon EC2)](http://aws.amazon.com/ec2 "Amazon EC2"):
This is our primary service and we will inspect this first. In brief this is the service that allows you to get a server (hardwarde + software full stack as needed) up and running in little time, assign an IP address to it, set firewall and invite users to the website. Well except for the invite part the rest are all provided by Amazon and over an API. So my PHP code coulf do that! Of course I will be billed for it.

[Amazon Simple Storage Service (Amazon S3)](http://aws.amazon.com/s3 "Amazon S3"):
Just store whatever you needed, setup access rules, and forget about it. Simple!

[Amazon CloudFront](http://aws.amazon.com/cloudfront):
This of these as the equivalent to you local post offices. So you do not need to go to the city central post office to fetch something. Local distribution of data! Its fast way to get things to the audience.
Well there are other services but I am not as good with them. When I experiment/use them enough I will blog on them.