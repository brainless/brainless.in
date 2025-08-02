---
id: tag:blogger.com,1999:blog-27384460.post-4315696470357375657
title: "Odd error with Redis, PHPRedis, Gearman, PHP"
pubDate: 2010-08-13
author: Sumit Datta
categories: ['php', 'gearman', 'redis']
---

We have a setup for background jobs for all the websites we manage like forums.com, files.com, payments.com, etc. The background jobs play around with lists of data which are stored in [Redis](http://code.google.com/p/redis/). We use [Tokyo Cabinet](http://1978th.net/tokyocabinet/) for our main data store though.  

The setup is somewhat like this:  

* PHP with [gearmand extension](http://pecl.php.net/package/gearman)
* [Gearmand](http://gearman.org/) (the daemon)
* PHP with [PHPRedis extension](http://github.com/owlient/phpredis)
* Redis daemon

Now our background workers were typical Gearman workers written in PHP. All was fine till the time we shifted list manipulation codes to background. Usually in background workers, we connect to all needed daemons (Tokyo Tyrant, Redis, etc.) and go into the Gearman wait loop.  

We never had any errors here until we brought in Redis. Earlier we used to manage lists of data in Tokyo itself with PHP based arrays. Now we were shifting to Redis lists. But we had this error coming to us (in the following form):  

**protocol error, got '%c' as reply type byte**  

We spent days on this and could not figure out why. We changed from PHPRedis to native PHP extensions, we had similar errors. Finally we had a hunch that the Redis connection was getting an idle timeout. The reason for such an assumption was that we had the errors every once a while and then we had all things fine again. Again after a while a few errors. But when we had errors we would lose data.  

We checked the configuration for Redis and found the fault. The connection timeout was set to 300, which we then changed to 0 (no timeout). Doing this fixed the errors. And all stuff work great now.  

Only if the errors from PHPRedis was a bit clearer, it would have been easier for us to catch the error.