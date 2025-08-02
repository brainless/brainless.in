---
id: tag:blogger.com,1999:blog-27384460.post-8122935386260418261
title: "Basic Gentoo on Amazon EC2"
date: 2009-05-15
author: brainless
categories: ['amazon', 'gentoo', 'ec2', 'elasticfox']
---

Continued from [Introduction to Amazon EC2 (Continued...)](/2009/05/introduction-to-amazon-ec2-continued.html)...
If you have come this far then I can assume you have an Amazon account, Firefox, Elasticfox extension on it. If not, well then you should get them to do this yourself or else just read through! Lets open Firefox and from the Tools menu on top you should see Elasticfox. On clicking it you should see a pretty detailed interface and a dialog box asking you to fill in your Amazon credentials. Go ahead and do that. Basically it needs a name (like a nick name, just for you to refer to that account), the Amazon Key, and Secret. The last two are string that you will find [here](http://aws-portal.amazon.com/gp/aws/developer/account/index.html?action=access-key) after you login with your AWS account.

Now if that step is done we should be able to select our new Amazon profile name in Elasticfox (at the very top center in the Elasticfox extension's UI). Done. Now you will see many tabs in Elasticfox. They are Instances, Images, KeyPairs, etc. Right now we are only interested in the KeyPairs tab. Click on it.You should see a blank list unless you already have created a key for yourself. Anyways for our purposes we will use the small green icon which says "Create a new keypair". We will need to give a name for this, say "brainless". What happens now is that Amazon creates a keypair for us, and sends the private part of the keypair. If all goes well Elasticfox will let us save the private part of the keypair (named "id-brainless" if we used "brainless" for the name of the keypair).

Now we have a keypair. If you have no idea about this keypair thing, well just do a search on it, like [here](http://www.google.com/search?q=ssh+keypair). Now in Elasticfox you see the tabs again. This time we need the Images tab. Click on the refresh button in the Images section. It will fetch a list of all images available at that moment. These images are basically like Live CD/DVD mediums. You use them to boot your own instance. Now there is plenty of choice here and you can make your own custom image too. You will notice a small search text box near the refresh button. Type in nginx. You should get an AMI with this AMI ID: ami-6138dd08. Notice that there is a Manifest name, which is pretty explanatory for many AMIs. Same for this one. It should say "ami.yyang.info/gentoo-nginx-php-mysql-06feb2008.manifest.xml", which means it comes with nginx, PHP and MySQL setup.

Now right click on that AMI. You will see a dialog box in Firefox. There are quite a few parameters, but we are right now interested in only a few. They are:
* Instance Type (basically this defines how powerful a server you need, refer [here](http://aws.amazon.com/ec2/#instance)). We choose m1.small here.
* Minimum number of instances (in case you want more than one server or instance started at once). We keep this as 1.
* Maximum number of instances (what is the maximum number of instances that Amazon should try to start at once). We keep this as 1.
* KeyPair (choose the brainless key here, the one we created just above).
* Just notice that in the Security Group section there is a "default" group in which this new instance will launch. This is the default parameter. We will come to this part soon.

Now click on Launch and pray! Well not really. Unless something is really wrong or Amazon is out of empty instance slots (very unlikely) you will have a shinny new instance all to yourself, with a fresh Gentoo booting on it as you are reading this!

Now notice the very important thing here. You did not do to a website to sign-up for a new server and got it in a few hours or maybe a day. Rather this is all through an API. In our case Elasticfox is consuming the APIs and we are using the GUI of Elasticfox. Later we will see the actual API and deal with it a bit to get an idea. And at an even later point I intend to blog on how to use Tarzan PHP AWS library to write a small scaling platform for your website. Yes auto scaling! Wallah!!!

Lets not get carried away though. So back to our instance. Where is it? Simple, check the Instances tab. You will notice a new row there with a lot of details. The most important one right now is State which I am sure you understand already. Well it simply tells what state the server is in: running, or pending (booting up), shutting-down, terminated (shutdown complete). Refer [here](http://docs.amazonwebservices.com/AWSEC2/latest/DeveloperGuide/ApiReference-InstanceStateType.html).