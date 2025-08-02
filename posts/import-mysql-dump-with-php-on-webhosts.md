---
id: tag:blogger.com,1999:blog-27384460.post-5430582065668541030
title: "Import MySQL dump with PHP on webhosts"
date: 2009-06-20
author: brainless
categories: ['webhost', 'php', 'mysql', 'sql import', 'godaddy']
---

Webhosts like GoDaddy and other similar often limit how much you can import with the online control panel (phpMyAdmin in most cases). So here is a simple PHP script that does this for you. You have to take a mysql dump from your database. Upload it to you host.

Make sure you change the mysql\_connect parameters to reflect your database server settings. The following line numbers need change:

1. line 2: mysql\_connect( ) parameters: Database host, username, password.
2. line 3: mysql\_select\_db( ) parameters: Database name.
3. line 4: fopen( ) parameters: path and name of you SQL dump file.

```

php
mysql_connect('host', 'user', 'password');
mysql_select_db('database');
$file = fopen('dump.sql', 'r');
print '<pre';
print mysql_error();
$temp = '';
$count = 0;

while($line = fgets($file)) {
  if ((substr($line, 0, 2) != '--') && (substr($line, 0, 2) != '/*') && strlen($line) > 1) {
    $last = trim(substr($line, -2, 1));
    $temp .= trim(substr($line, 0, -1));
    if ($last == ';') {
      mysql_query($temp);
      $count++;
      $temp = '';
    }
  }
}
print mysql_error();
print "Total {$count} queries done\n";
print '
```
';

You may use the code for any purposes
What I have done is simply read the dump line by line. Lines starting with -- or /\* are considered comments and left out. Now we need to build full SQL commands which span across many lines in the dump. So we check for the end semicolon (;) and until we find one we just join the lines together to get one SQL statement. Once done we execute it and move on to the next.

If you find any errors please comment. Also if you port this to use PostgreSQL or use other programming languages please share your code's link on this post's comment.