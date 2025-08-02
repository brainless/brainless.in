---
id: tag:blogger.com,1999:blog-27384460.post-961443921870221179
title: "Basic security setup on AWS"
date: 2011-08-08
author: brainless
---

Recently at [MobStac](http://mobstac.com/) we restructured our layout of [EC2](http://aws.amazon.com/ec2/) on [Amazon Web Services](http://aws.amazon.com/) so that we are more secure than earlier. We wanted a scheme that would not be painful for our current deployment scheme but would still be as strict when it comes to inward access as possible.  

Here is what we settled down for:  

Application servers (Django) are all internal security group accessible only. So they can not be accessed from outside our own servers.  

RDS (our MySQL storage of choice) is allowed incoming from only the application group.  

There is a separate Deployment EC2 that has SSH access allowed from the rest of the world. You login here and do a deploy.  

When deployment occurs it fetches extra credentials needed to access the more secure application instances. These credentials are kept in some repositories which almost no one has access too. They credentials include key-pairs, passwords and stuff. They are patched in to the code on the fly and deployed to application instances.  

This means deployment can happen only from one instance. And no instance other than this one is accessible from outside.  

Also there are background workers instances which has security settings as strict as application instances or even tighter.