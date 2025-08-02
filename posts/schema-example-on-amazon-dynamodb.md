---
id: tag:blogger.com,1999:blog-27384460.post-543094932901261510
title: "Schema Example on Amazon DynamoDB"
date: 2012-01-20
author: brainless
categories: ['amazon', 'aws', 'dynamodb']
---

First an apology to anyone who read my previous blog post. I had used wrong rates for throughput capacity. I noticed this since my calculations seemed a little costly :)  

Throughput Capacity price as on [AWS website](https://aws.amazon.com/dynamodb/pricing/), as of today:  

\* Write Throughput: $0.01 per hour for every 10 units of Write Capacity  

\* Read Throughput: $0.01 per hour for every 50 units of Read Capacity  

Thus as per my example of 7 tables with minimum 5 Read and 5 Write throughput capacity per table, hourly pricing is:  

35 \* $0.001 = $0.035 (Write)  

35 \* $0.0002 = $0.007 (Read)  

Total hourly cost = $0.042, monthly cost = $30.24  

My current database design is using 3 tables. One is for authentication. We will allow users to signup/login using either email+password (MD5) or using FB Connect or similar. In both cases we will store these authentication string(s) in an "Auth" table. The Primary Key will be the auth strings themselves, either concat of email+password or OAuth tokens. The items will have another attribute which will be `UserName`.  I am yet to read FB Connect documentation, so this may need slight re-configuration.  

The `UserName` is a PK in the second table which is "User". The items contain common user attributes like `FirstName`, `LastName`, `Email` and many such needed data. The last table is the "Campaign" table where we store campaign configure information for [Mag](https://mag.io/). This has a [Hash and Range type Primary Key](http://docs.amazonwebservices.com/amazondynamodb/latest/developerguide/DataModel.html). The Hash part is the `UserName`, and the Range is the `CampaignId` (unique string generated from the title of the Campaign). Each user can run multiple Campaigns. What I am not sure of is what is the performance hit if all users mostly have only 1 campaign. In that case I think it will be better to store Campaigns as a Set in the "User" table and the "Campaign" table could have just a simple Hash PK named `CampaignId`.  

My doubts as of now are what values to set for throughput. I neither want to overcharge myself, nor do I want AWS to throttle the connection. I guess a real example will shine more light. Back to coding now!