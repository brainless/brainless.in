---
id: tag:blogger.com,1999:blog-27384460.post-7380102558218236094
title: "S3 storage for Django"
date: 2011-08-08
author: brainless
---

Hi there!  

Am blogging after a few months now. I have settled in the [MobStac](http://mobstac.com/) team as an all hands engineer. I have shifted to Bangalore with 2 friends from Kolkata.  

Anyway, at MobStac we needed an S3 storage backend for our [Django](https://www.djangoproject.com/) app (Django runs our publisher platform, and mobile site serving platform). I figured out there is nice way to write a [custom storage backend](https://docs.djangoproject.com/en/dev/howto/custom-file-storage/). But then a bit searching and I came across [django-storages](https://bitbucket.org/david/django-storages/wiki/Home) by David. It supports for backend than we needed, so I just took out the s3boto code and it was easy as cake.  

So now all media uploaded goes to S3, and honestly integrating this in Django was smooth as silk.