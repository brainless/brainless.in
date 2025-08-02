---
id: tag:blogger.com,1999:blog-27384460.post-114684837295855096
title: "Roadmap for GData module work"
date: 2006-05-05
author: brainless
---

How to successfully complete this project ?  

Well the answer follows as a roadmap:  

1. Atom module presents the features of Atom syndicating protocol and
 it seems like a good place to start experimenting.

- Need to specify which parts of drupal
 is exposed through GData mudule. We also need to consider
 read-only and read/write parts seperately.

- Tweaking Atom module to
 make it take in requests as GData specifies.

- Creating a gfeed.php
 which actually takes all client request and turns them onto drupal.

- Test the gfeed.php and GData
 module across certain test conditions.

Till this I expect I need a month's time, by which we may even have better
 solutions to the HTTP PUT / DELETE and gfeed.php issues.  

1. Support for basic query
 stuff through the GData module. ( remember the 'q' thing ? )
2. Atom has a publishing protocol too, which however is not implemented
 in Atom module, but is needed in GData. Thus the GData module now needs
 to grow into supporting updations,
 insertions, deletions.
3. Implementing authentication
 in GData. I except by this time Google will have done more work on this
 end and impletemention will be easier.
4. Testing as usual.

Again this above block should be a month's work.  

1. Optimise the module's query
 part so that it is less time and resource consuming.
2. Allow the community to test the mudule and go into a full bug-fixing
 mode.

At the end of this we should have a full working GData module for Drupal.