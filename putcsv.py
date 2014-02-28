# -*- coding: UTF-8 -*-


import MySQLdb as mdb
import sys
import csv


#获取mysql的链接对象
con = mdb.connect(host='1.1.1.1',user='12345',passwd='12345',db='test');

with con:
    #获取执行查询的对象
    cur = con.cursor()

    #执行那个查询，这里用的是select语句
    cur.execute("select 1,2,3 from test")

    #使用cur.rowcount获取结果集的条数
    numrows = int(cur.rowcount)
    print numrows  #断行调试语

    #循环numrows次，每次取出一行数据
    for i in range(numrows):
        #每次取出一行，放到row中，这是一个元组(id,name,pic)
        row = cur.fetchone()
        rows = row
        
        
        #print row[0], row[1],row[2]
        #print rows
        

with open('eggs.csv', 'wb') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['1'] + ['2'] + ['3'])
    spamwriter.writerow(rows)
