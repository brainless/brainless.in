---
id: tag:blogger.com,1999:blog-27384460.post-2632282161239120337
title: "Building a Yii app: The Data Model"
pubDate: 2012-02-17
author: Sumit Datta
categories: ['yii', 's3', 'php', 'development']
---

A friend of mine needs a web application to be revamped. I had originally created it about 2 years back using a custom PHP mini-framework that I had built for many projects at that time. The development had stopped for different reasons and parts of his web application were incomplete. For example images were not upload to [Amazon S3](http://aws.amazon.com/s3/), which was originally planned. Some Model edits were not working in many parts and there were some data validation issue. He has been doing the groundwork for his business and now has decided to finally complete the application.  

The application is related to Medical needs, information about patients, doctors, hospitals etc. I have decided to make the new version using [Yii](http://www.yiiframework.com/), since some other developer will take over if the project is successful and Yii (or other popular frameworks) is a very well documented framework for anyone to use. The choice of Yii against other PHP frameworks is rather just an impulsive one. I have read comparisons of the good PHP frameworks and Yii is among the top few. Anyway moving on...  

While I am building this application, which is a moderately feature rich one, I intend to write about my experiences. Hope this helps anyone looking for a quick introduction and example for Yii. I am trying to make this a tutorial for Yii, I will try my best here. The project needs data for multiple types:  

* General User Profile (could be a patient)
* Doctor
* Hospital
* Nursing Home
* Other Medical companies like: Medical Shop, Diagnostic Center, Fitness Center, Ambulance Provider, Nurse, etc.

Other information include:  

* Specialization: this is related to Doctors, explained below
* Address: City, State, Country, etc. Any entity can have multiple addresses
* Phone: can be either a fixed or a mobile (cellular) phone. Any entity can have multiple phones, also address can have phones associated with them
* Department: Hospitals or Nursing Homes can specify many departments
* Branch: Hospitals, Nursing Homes of Other companies can have multiple locations/branches.
* Image: multiple images for any entity.
* User: this is used for authentication, simple email/password for now.

In order to manage the mappings of many entity types to Address, Phone, Branch, Image etc. I have used a [central Entity table](http://stackoverflow.com/questions/2862918/common-one-to-many-table-for-multiple-entities). Every type of physical entity has an entry in the Entity table (including each branch). Then Address, Phone, Branch, Image, Department are mapped to Entity table.  

In Yii terms the relations look like this:  

* Doctors can have one or more Specialization (HAS\_MANY in Yii Model)
* Doctor, Hospital, Nursing Home, Other, Profile have a one-to-one mapping to Entity (BELONGS\_TO in Yii)
* Entity can have multiple Addresses, Phones, Images (HAS\_MANY in Yii)
* Entity can have many Departments (HAS\_MANY). This is limited to only Hospital, Nursing Home or Other types though at the application level.
* Entity can have another Entity as Branch (HS\_MANY). This is also limited to Hospital, Nursing Home or Other types at the application level.

I will write about setting up Yii Models in the next blog entry...