---
id: tag:blogger.com,1999:blog-27384460.post-7921552726455540962
title: "Day One of Amazon DynamoDB"
date: 2012-01-20
author: brainless
categories: ['amazon', 'development', 'aws', 'pricing', 'dynamodb']
---

Its been just about a day that I have been going through the documentation of the newly released [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). Using the PHP SDK and getting a basic Table up was simple. Right now I am planning the data organization. DynamoDB is a schema less data store. There is a primary key per table which is your main query column, so as to say. I am trying to use existing MongoDB [based](https://github.com/jamm/DataMapper) [data mappers](http://fatfree.sourceforge.net/page/data-mappers) and modify them for DynamoDB.  

I am planning to use [Fat-Free Framework](http://fatfree.sourceforge.net/) for the back-end. This is basically the management panel's API. All user interface will be JavaScript only, within the browsers. Templates will probably be Mustache. Anyways, back to DynamoDB: once I get a data mapper done, I will release it on GitHub. I am also looking for similar stuff in Python and Node. I am sure in a couple of weeks we will see them pouring over the Internet.  

**Pricing**  

I have been doing some pricing calculations. This is important for us since we have a tiny budget to start with. The price of AWS DynamoDB depends on two main things: size of data store and the throughput needed. The size is charged by the GB/month. So a decent 5 GB data store will cost $5/month. But remember there is metadata that AWS stores and you will be charged for that. I will get a better overall idea of the numbers involved gradually but for starters here is the note from AWS site:  

"Amazon DynamoDB is an indexed datastore, and the amount of disk space your data consumes will exceed the raw size of the data you have uploaded. Amazon DynamoDB measures the size of your billable data by adding up the raw byte size of the data you upload, plus a per-item storage overhead of 100 bytes to account for indexing."  

The other cost involved is the throughput. This is total reads/writes per second you will need, across all your tables. The [minimum throughput allowed per table is 5 each](http://docs.amazonwebservices.com/amazondynamodb/latest/developerguide/Limits.html) (5 read and 5 write). That means that if you initially have say 7 tables, then your minimum throughput is (7 \* 5) + (7 \* 5) = 70.  

Price for read throughput is $0.01/hour for 10 units.  

And price for write throughput is $0.01/hour for 5 units.  

Thus your total hourly price comes to $0.07 + $0.035 = $0.105/hour.  

Assuming 720 hours in a month, your monthly cost for throughput is $75.6.  

This pricing is a little steep. Which is itching me to go through the schema design and see what our starting costs are. I had initially not taken the minimum throughput **per table** into account; which was yesterday. Anyway, I will need a complete table design to judge anything. But one thing is clear: table count is costly if your tables are basic and do not need even 5 writes/reads per second.  

Edit: I had calculated the sum to be $0.15 / hour. I am still not out of bed I guess :)