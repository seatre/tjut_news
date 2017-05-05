# encoding: utf-8
# Created by seatre on 2017/5/5

import mysql.connector


# 实现了在数据库存储的功能
class TNPipeline(object):
    def __init__(self):
        self.con = mysql.connector.connect(user='seatre', passwd='basexzf!', host='47.92.27.138', db="tjut_news",
                                           charset="utf8")
        self.cursor = self.con.cursor()
        # self.cursor.execute('use python')
        # self.cursor.execute('create table manhua(name varchar(100) primary key,duty varchar(200),location varchar(200),time varchar(100),sallary varchar(100))')

    def process_item(self, item, spider):
        # 定义插入数据的功能
        # self.cursor.execute("insert into manhua(name,duty,location,time,sallary) values(%s,%s,%s,%s,%s)",(item['name'],item['duty'],item['location'],item['time'],item['sallary']))
        # clothes_name
        self.cursor.execute(
            "insert into JD(id,title,dt,url) VALUES (NULL,%s,%s,%s)",
            (item['news_title'], item['news_datetime'], item['news_url']))
        self.con.commit()  # 这是必须要提交的
        return item  # 必须要返回一个item
