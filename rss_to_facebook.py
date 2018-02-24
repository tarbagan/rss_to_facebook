# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:11:04 2018
Parser and posting to facebook
@author: Irgit V/A
"""
import feedparser
import pymysql.cursors
import facebook
import time

graph = facebook.GraphAPI(access_token="you token")

#parsing links news with pictures, without skipping pass
link1 =  set()
url = feedparser.parse("URL RSS")
for e in url["entries"]:
    if e.get('imgurl','') != "no image": #for beauty we take only pictures with the image
        link1.add(e.get('link',''))

#connect mysql, get links
connection = pymysql.connect(host='localhost',
                             user='*****',
                             password='*****',
                             db='*****',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
link2 = set()
cur = connection.cursor()
cur.execute("SELECT  *****,  ***** FROM ***** ORDER BY ***** DESC")
for row in cur:
    link2.add(row.get('url'))
cur.close()

#compare lists
link3 = set()
diff_links =  link1.difference( link2)
if  diff_links:   
    for link in diff_links:
        link3.add(link)
        fblink = link
        graph.put_object(parent_object="me", connection_name="feed",  link=fblink)
        time.sleep (5)
        
        #save to MySQL
        with connection.cursor() as cursor:
            cursor.executemany("INSERT INTO `****`(`url`) VALUES (%s)", link3 )
            connection.commit()  