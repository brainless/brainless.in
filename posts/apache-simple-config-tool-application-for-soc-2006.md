---
id: tag:blogger.com,1999:blog-27384460.post-114654714216668604
title: "Apache Simple Config Tool Application for SoC 2006"
date: 2006-05-02
author: brainless
---

Name :  

 Sumit Datta  

Email :  

 sumitdatta@gmail.com  

Project Title :  

 Simplifying Apache configuration  

Synopsis :  

 The intention of this project is to make a tool or application which will greatly simplify the configuration process for Apache web server once it has been installed. The tool can be compared to phpMyAdmin (which exists for MySQL). phpMyAdmin is extensive in its approach in helping users to use a MySQL database server. It does not imply that users cannot access MySQL without phpMyAdmin, but that it makes maintance a lot easier. Content on the internet is not created only by those who can understand details of .htaccess files. People from non-tech spheres create a lot of content. They have to maintain web sites too. The process of learning details of Apache configs without a useful GUI is a burden to most such people. A tool which will help in the process is very much needed.  

Benefits to the Community :  

 Through this project I intend to create a tool (for example a PHP/Perl/Python based GUI application) which will simplify the process of configuring the Apache web server. The project can also be extended to make Apache log files easier and more helpful to general non-technical audience.  

Deliverables :  

 An application written in either PHP/Perl/Python or a combination which enables easy GUI based configuration of Apache web server. Also I may implement an extension to make log files more understandable / readable and useful to the general user.  

Project Details :  

 The GUI tool (like phpMyAdmin) will help configure and understand the settings of Apache web server. It will have forms in easy english (maybe other languages too) which ask questions like: What is the domain name of this site or Where are the files located for X website, etc. Question forms have to be well designed so that user dont get confused, or overwhelmed by the number of questions. The tool will have to use inbuilt facilities available in the programming languages or environment (like $\_SERVER['SERVER\_NAME'] and similar data through PHP) to provide useful options and suggestions to the user.  

 Config options can be generate when requested by the user so that he/she can copy and paste them to a .htaccess file.  

 A second module can be addedd which provides some important imformation from Apache log files (like browsers, host IP, etc). This is available in other specific tools, but adding to this config tool will make a nice module.  

Project Schedule :  

 The project will take about a month's time. Then we can release a beta and wait for suggestions. For this kind of tool there will be immense user suggestions. The next pahse of more than a month will be spent on suggestions, improvements and bug fixes. Once the tool is stable, I can move onto creating module for log file handler.  

Bio :  

 I am a student of Computer Science from India. I am a part time PHP/MySQL based web developer. I have previously worked for Intrasoft Technologies (www.123greetings.com : yes it runs from India !). There I worked on making an internal content management system which was tightly linked to the employee structure of the company. Through that I have gained lot of insight into how easy it should be to put up content on Internet. But sadly it isnt. I have worked with artists and creative artists who create wonderful content for the net, yet dont mind giving a few extra blank spaces in filenames. Internet is for the masses and I understand how important it is for tools to exist which help ordinary people to create and manage content and sites. I am myself working on a plan for a CMS which takes into account my past experiences and current state of internet. Ofcourse again my emphasis is to empower the common man to be content creator and maintainer. I have been associated with Open Source projects for about 2 years now, but contribution is not satisfactory according to my judgement. I want to do something really useful (like this project) for the common content creators of the world. I have a C,C++ background but I live in internet technologies.  

Thanks