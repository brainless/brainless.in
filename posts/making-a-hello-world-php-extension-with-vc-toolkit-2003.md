---
id: tag:blogger.com,1999:blog-27384460.post-115218475799928473
title: "Making a Hello World PHP extension with VC++ Toolkit 2003"
date: 2006-07-06
author: brainless
---

I wanted to do some PHP Extension making and so started googling around for help. Most help is about using VC++ 6.0 or have project files for the full VC++ IDE. Since I have the Toolkit compiler I thought I would read the help available and do a compile from the Toolkit Command Prompt.  

My basic need for PHP Extensions is that I want to make a Drupal ([drupal.org](http://drupal.org)) core extension. Just experimental stuff. So the C file is a simple Hello World type which just prints "Hello Drupal World"  

the C code is:  

/\* include standard header \*/  

/\* you will need to include this in all of your php extension projects\*/  

#include "php.h"  

/\* All the functions that will be exported (available) must be declared \*/  

ZEND\_FUNCTION(drupal\_world);  

/\* Just a basic int to be used as a counter\*/  

/\* function list so that the Zend engine will know what’s here \*/  

zend\_function\_entry drupalmod\_functions[] = {  

 ZEND\_FE(drupal\_world, NULL)  

 {NULL, NULL, NULL}  

};  

/\* module information \*/  

zend\_module\_entry drupalmod\_module\_entry = {  

 STANDARD\_MODULE\_HEADER,  

 "Drupal",  

 drupalmod\_functions,  

 NULL,  

 NULL,  

 NULL,  

 NULL,  

 NULL,  

 NO\_VERSION\_YET,  

 STANDARD\_MODULE\_PROPERTIES  

};  

#if COMPILE\_DL\_DRUPAL\_MOD  

 ZEND\_GET\_MODULE(drupalmod)  

#endif  

ZEND\_FUNCTION(drupal\_world) {  

 zend\_printf("Hello Drupal World");  

}  

It was mostly taken from : <http://www.zend.com/apidoc/zend.creating.php>  

To compile this I had to start experimenting with all available help instructions ( that relate to using the VC++ IDE and not a Command Prompt Toolkit ). Anyways the final command that worked is:  

cl drupal.c /D "WIN32" /D "ZEND\_DEBUG=0" /D "COMPILE\_DL\_DRUPAL\_MOD" /D "ZTS=1" /D "ZEND\_WIN32" /D "PHP\_WIN32" /LD /EHsc /nologo /I"F:\coding\php-4.4.0\main" /I"F:\coding\php-4.4.0\Zend" /I"F:\coding\php-4.4.0\TSRM" /I"F:\coding\php-4.4.0\win32" /I"F:\coding\php-4.4.0" /I"F:\coding\php-4.4.0\regex" "C:\php\php4ts.lib"  

As you can understand probably /D makes preprocessor defines.  

My course is at F:\coding\php-4.4.0  

My running PHP is at C:\php which is also same version (4.4)  

drupal.c in the file I wrote for the extension and whose source is above.  

I ran this from the VC++ 2003 Toolkit Command Prompt  

My workind directory was F:\coding\php-4.4.0\ext\drupal where the file drupal.c exists. you dont have to keep the file there. You can place it anywhere and compile.
Just remember to change the paths in the above command. Thats all  

After successful compile you will find a drupal.lib file and drupal.dll file in the folder from where you are compiling. copy the dll and use it as usual (you can rename it to php\_drupal.dll or use the compilers output options to name the output dll file)