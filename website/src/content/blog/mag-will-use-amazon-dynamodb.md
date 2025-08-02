---
id: tag:blogger.com,1999:blog-27384460.post-9091016189194743025
title: "Mag will use Amazon DynamoDB"
pubDate: 2012-01-19
author: Sumit Datta
categories: ['amazon', 'development', 'mag', 'aws', 'dynamodb']
---

Amazon's latest announcement (and offering) could not have come at a better time for [Mag](https://mag.io/). I am talking about Amazon DynamoDB here and I feel it is a good fit for Mag.  

For the last few weeks I have been looking at many available options for the data storage for Mag. Notice I mentioned data store and not RDBMS. The reason is that Mag's data is really a large collection of configurations for campaigns that our clients run. Yes they may grow in size as we add customers, but the schema is quite simple, at least for now. And I would prefer having a hosted, cost effective service that is fast. I want to concentrate on the application because that is the real power of Mag.  

My current choices included the NoSQL systems like MongoDB, Couch, Redis or similar, but honestly I would not want to handle managing the storage myself. And replication, and other stuff. I had made plans to do that though, but now I will be free from them. Plus the move to SSD seems very practical and needed. I am not saying SSDs will help Mag right now, but from the industry standpoint this is a good start.  

But what has really made my decision easy is that it is no hassle, no management and it scales when needed. AWS also claims really low latency, very high throughput. Although our reads/writes will be tiny to start with. I will see the latency for myself once I start but I believe their claims for now. From a startup point of view the pricing is good too. Initially free to start with, although its a tiny 100MB database, but its good to experiment stuff. I used basic assumptions to check prices and it seems good to me.  

I will see what existing libraries I can re-use to make the transition smooth. Our applications are JavaScript heavy, the back-end (PHP/Python/Node mix) is just an API as such. All rendering done right on the browser. Just JSONs passing here and there. That's it then, lets code!