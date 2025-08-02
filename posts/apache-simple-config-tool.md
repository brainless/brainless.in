---
id: tag:blogger.com,1999:blog-27384460.post-114651179166786858
title: "Apache Simple Config Tool"
date: 2006-05-04
author: brainless
---

Simplifying Apache configuration :  

The intention of this project is to make a tool or application which will greatly simplify the configuration process for Apache web server once it has been installed. The tool can be compared to phpMyAdmin (which exists for MySQL). phpMyAdmin is extensive in its approach in helping users to use a MySQL database server. It does not imply that users cannot access MySQL without phpMyAdmin, but that it makes maintance a lot easier. Content on the internet is not created only by those who can understand details of .htaccess files. People from non-tech spheres create a lot of content. They have to maintain web sites too. The process of learning details of Apache configs without a useful GUI is a burden to most such people. A tool which will help in the process is very much needed.  

Benefits to the Community :  

Through this project I intend to create a tool (for example a PHP/Perl/Python based GUI application) which will simplify the process of configuring the Apache web server. The project can also be extended to make Apache log files easier and more helpful to general non-technical audience.  

Deliverables :  

An application written in either PHP/Perl/Python or a combination which enables easy GUI based configuration of Apache web server. Also I may implement an extension to make log files more understandable / readable and useful to the general user.  

Project Details :  

The GUI tool (like phpMyAdmin) will help configure and understand the settings of Apache web server. It will have forms in easy english (maybe other languages too) which ask questions like:  

What is the domain name of this site or Where are the files located for X website, etc. Question forms have to be well designed so that user dont get confused, or overwhelmed by the number of questions. The tool will have to use inbuilt facilities available in the programming languages or environment (like $\_SERVER['SERVER\_NAME'] and similar data through PHP) to provide useful options and suggestions to the user.
Config options can be generate when requested by the user so that he/she can copy and paste them to a .htaccess file.  

A second module can be addedd which provides some important imformation from Apache log files (like browsers, host IP, etc). This is available in other specific tools, but adding to this config tool will make a nice module.  

[See a sample form for the Apache conf tool](http://sumit.pixlie.com/2006/05/sample-settings-form-for-apache-simple.html)  

[Simplifying Apache configuration?](http://www.mattcutts.com/blog/simplifying-apache-configuration/)(Original blog post on this idea from Matt)
More comes here (details particular for SoC)