#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import xlwt #操作excel模块

import sys

import pymysql #数据库连接 - PyMySQL 驱动



# 打开数据库连接

mydb = pymysql.connect("localhost","root","cuishuai","linuxTest" )

file_path = sys.path[0]+'/统计名单.xls'#sys.path[0]为要获取当前路径，filenamelist为要写入的文件

f = xlwt.Workbook(encoding='utf-8', style_compression=0) #新建一个excel

sheet = f.add_sheet('sheet1') #新建一个sheet

pathDir = os.listdir(sys.path[0])#文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录

i = 0 
print("------------------欢迎使用文件统计辅助工具-----------------")

print("    数据统计中...........................")

# 使用cursor()方法获取操作游标 
mycursor = mydb.cursor()

for s in pathDir:
	
    if ( s == 'data.py' ):
        continue
    sheet.write(i, 0, s) #参数i,0,s分别代表行，列，写入值
    # SQL 插入语句
    sql = """INSERT INTO homework(fileName)VALUES ('{}')""".format(s)
    
    try:
   	# 执行sql语句
        mycursor.execute(sql)
   	# 提交到数据库执行
        mydb.commit()
	print("第"+str(i+1)+"条数据录入成功！")
    except:
  	 #捕获异常
        mydb.rollback()

    i = i+1

#遍历文件名到终端	
for name in pathDir:
	if ( name == 'data.py' ):
		continue
	print(name)


print("统计数据文件位于："+file_path)

#显示文件名数量
print("#################目前提交"+str(i)+"人########################")        

#保存文件
f.save(file_path)

# 关闭数据库连接
mydb.close()

