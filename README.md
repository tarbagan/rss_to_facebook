# rss_to_facebook
A small code that allows you to parse the RSS feed and send it to the Facebook wall. The code is very compact, suitable for Python 2.7 and Python 3.6

To check the RSS of the stream, you save to the Mysql database

#Install

1) Create a mysql table with the 'ID' (AUTO_INCREMENT), 'url'
CREATE TABLE tuva (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, url VARCHAR(255))
2) Get access_token Facebook
3) Configure the script
4) Configure Cron

Demo https://www.facebook.com/tuva24.ru/
http://tuva24.ru/

Autor: Irgit Valery https://github.com/tarbagan

"""
Parser and posting to facebook
"""
