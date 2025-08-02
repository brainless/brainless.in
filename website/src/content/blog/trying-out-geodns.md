---
id: tag:blogger.com,1999:blog-27384460.post-1661372149187067498
title: "Trying out GeoDNS"
pubDate: 2012-01-23
author: Sumit Datta
categories: ['dns', 'amazon', 'zerigo', 'mag', 'hosting']
---

For the last 3 weeks that we have started working on [Mag](https://mag.io/), we have been talking to a few prospective clients or other knowledgeable folks out there. We want to understand how individuals, SMBs or larger organizations use Social Media or the Internet in general. Of course all of these initial meets are local to Bangalore and a few in other cities in India (over the phone).  

We have been getting a very positive response and although we are building a truly global product we want to first cater to people nearby, learn and expand gradually. Thus it becomes important that we serve the Indian Internet audience. Now servers hosted in the US have high latency from India (~300 ms). Of course we host and will continue to host core business data on [Amazon Web Services](http://aws.amazon.com/) (we [have selected](http://0.0.7.220/01/mag-will-use-amazon-dynamodb.html) [DynamoDB](http://aws.amazon.com/dynamodb/)), but an Indian serving facility needs to exist (I will talk about serving details later). So one of the first things that popped up in my mind is that this should not be India specific architecture. Not an in.mag.io domain and such stuff. We should have a simple strategy that can scale in any region. Thus enter GeoDNS.  

GeoDNS or Geographical DNS is basically responding to user DNS queries with different responses, depending on the origin of the user request. So if I have a server, say per continent, then any user from any continent should be served from the server in that continent. The concept is simple to understand although I am sure its not an easy engineering task. This is where [Zerigo](https://www.zerigo.com/) [helps out](https://www.zerigo.com/news/launch-of-geodns-geolocation-load-balancing). We have used their DNS plans earlier (although Free plan), but GeoDNS is available only on DNS Pro plan. So I quickly upgraded and got a taste of the administration and a demo setup. The setup is easy: you just mention that a particular domain (or sub domain) is under GeoDNS. Then you assign actual server IP addresses per region with a special sub-domain starting with underscore (\_).  

Example:  

\_asi.test.mag.io   

\_def.test.mag.io   

The \_def is default, and \_asi is for Asia. If you query from Asia, you should that the \_asi IP address, else the default. The test worked perfectly fine. You can use a country code too (ISO two letter code) and USA is further divided in 4 regions. Very nice for traffic balancing by region. If you have similar needs, go ahead and try this :)