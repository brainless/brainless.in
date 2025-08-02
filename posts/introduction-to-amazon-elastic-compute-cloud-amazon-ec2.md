---
id: tag:blogger.com,1999:blog-27384460.post-1883397290885334261
title: "Introduction to Amazon Elastic Compute Cloud (Amazon EC2)"
date: 2009-05-13
author: brainless
categories: ['amazon', 'aws', 'ec2']
---

Continued from [Dummies Introduction to Amazon Web Services](http://brainlessphp.blogspot.com/2009/05/dummys-introduction-to-amazon-web.html)...
Imagine you need a web server. The hardware and the software, all together. You have a website which is growing in users and you want to make sure that the site grows along with the user numbers, that there is no downtime, and that the website stay as fast. You have a few things to do:

* Optimize the codes that run your website
* Optimize your software stack
* Get a better hosting account or a bigger server hardware
* Get more servers

Its the last two points we are interested in right now. Getting a better hosting account is easy if you have shared hosting account. If you have a dedicated server or a vds (virtual dedicated server) this is still easy task. But you may have to wait each time you want to upgrade your web server because it takes time to setup. Thus you need to plan ahead and take extra hardware so then when there are abrupt website peaks your site does not stop working.

Now since we are discussing EC2s which are like dedicated pieces of hardware we will assume the website does not run on shared hosting. So we are comparing with dedicated hosts or vds. Now getting extra servers is easy to say, but it costs if you want to predict usage (a digg effect, slashdot) and get extra servers. Also how much usage will you get? These maybe difficult numebrs to predict. It would be a lot easier if you could get servers when you need then, no hassle of installing you full software stack, and get it ready in a few minutes. Seems like the heaven of web serving? Well that is what EC2s are all about.

To start on what EC2s do in detail and how to use them from PHP (and other languages) its good to first read on Amazon's details about them (taken from their EC2 page, I was tired :P).

To use Amazon EC2, you simply:

* Create an Amazon Machine Image (AMI) containing your applications, libraries, data and associated configuration settings. Or use pre-configured, templated images to get up and running immediately.
* Upload the AMI into Amazon S3. Amazon EC2 provides tools that make storing the AMI simple. Amazon S3 provides a safe, reliable and fast repository to store your images.
* Use Amazon EC2 web service to configure security and network access.
* Choose which instance type(s) and operating system you want, then start, terminate, and monitor as many instances of your AMI as needed, using the web service APIs or the variety of management tools provided.
* Determine whether you want to run in multiple locations, utilize static IP endpoints, or attach persistent block storage to your instances.
* Pay only for the resources that you actually consume, like instance-hours or data transfer.

You will find those and other details on [this page](http://aws.amazon.com/ec2/)