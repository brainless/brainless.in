---
id: tag:blogger.com,1999:blog-27384460.post-5103344692691723860
title: "Trying out non AWS options"
pubDate: 2012-02-04
author: Sumit Datta
categories: ['vps', 'webhost', 'dedicated server', 'aws', 'hosting']
---

I have been using Amazon Web Services for all of my (or companies' I work with) compute or storage needs for the last 4 years. That include AWS S3, EC2, SimpleDB and even RDS (at MobStac). For the last few weeks I have been planning the platform choices for Mag. It does include AWS DynamoDB, S3 and EC2, but the picture is a bit different.  

Amazon DynamoDB guarantees a lot of performance and I personally do not want to take database headaches. DynamoDB pricing model is great to start with too. It is not cheap, but does not bite at the same time. And you continue paying as you grow. The data model is similar to other NoSQL services and you can shift out later if you want.  

AWS S3 is a really reliable, cheap storage solution and there is no doubt we will use it wherever we need. EC2 is great for its scalability or its powerful solution to failure handling. Bringing up a pre-configured EC2 (many data centers around the world) is fast, easy and cost per hour is cheap.  Also extra processing as and when needed is perfect fit for EC2 Spot Instances.  

While AWS EC2 provides all these great services, hosting regular websites and serving traffic is still costlier. Bandwidth is premium inside AWS. Yes they are very well connected, but you can get that from many top quality hosting providers/data centers. Also the machines themselves are not as fast as a good VPS could be. I have been searching for VPS providers with SSD storage, newer processors and RAM. Recently I tested a tiny VPS (384MB RAM) with such configuration and the Apache Benchmark shows better performance than an AWS EC2 instance (Ubuntu, nginx, PHP, APC, apc.stat=0). Although PHP on the VPS was compiled, and I will re-run the tests, but the difference was very visible.  

Of course I do not intend to co-locate or manage any hardware. But I certainly want to look at good VPS or unmanaged dedicated offerings. Configuring a VPS/server is not easy too, from firewall to internal network if you run a cluster, but if the pricing differences are worth it, then it makes business sense. And EC2 is never out of the picture. They will be used in parallel but for stuff I mentioned above and not for regular traffic.