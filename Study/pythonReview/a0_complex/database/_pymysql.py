#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/02
# file: MysqlModel.py
# Email:
# Author: rakiwine

import pymysql

# 创建数据库连接 增加参数 autocommit = 1 ，当发生update等操作时，会实时更新到数据库内。
connection = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="Root_123", db="poker")
# 获取一个游标对象
cursor = connection.cursor()


# 通过python脚本向mysql数据库插入单条数据
def insert_one():
    # 直接用execute方法执行sql语句
    cursor.execute('insert into student(id,name,age) values (123456,"tom",12)')
    connection.commit()

    # 将sql语句单独出来，在语句中用%s做占位符
    sql = "insert into student values(%s,%s,%s)"
    param = (23456, 'lilei', 20)
    cursor.execute(sql, param)
    connection.commit()


# 过python脚本向mysql数据库批量插入数据
def insert_many():
    # 26万条数据，需要约1.5小时，使用第二种方法只需要10几秒 不建议
    # for i in range(1, 10):
    #     param = str(i)
    #     sql = "insert into student values(%s,'yy',20)"
    #     cursor.execute(sql, param)
    #
    # connection.commit()

    for i in range(1, 10):
        param = str(i)
        sql = "insert into student values(%s,'yy',20)"
        cursor.execute(sql, param)
        connection.commit()

    # 26万条数据，需要10几秒
    sql = "insert into student values(%s,%s,%s)"
    # [(111111, 'haha', 13), (22222, 'hehe', 34)]
    param = ((111111, 'haha', 13), (22222, 'hehe', 34))
    # 使用executemany方法批量插入数据
    cursor.executemany(sql, param)
    # 提交
    connection.commit()

# cursor执行命令的方法
# 1、callproc(self, procname, args):用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
# 2、execute(self, query, args):执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
# 3、executemany(self, query, args):执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
# 4、nextset(self):移动到下一个结果集

# cursor接受返回值的方法
# 1、 fetchall(self): 获取查询返回的全部结果 将结果保存到tup，每条结果都是元组类型，所有的元组组成了一个元组集
# 2、 fetchmany(self, size=None): 接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
# 3、 fetchone(self): 返回一条结果行.
# 4、 scroll(self, value, mode=‘relative’): 移动指针到某一行.如果mode=‘relative’,则表示从当前所在行移动value条,如果mode=‘absolute’,则表示从结果集的第一 行移动value条.

# 查询
result = cursor.execute("")
# ((),(),(),())
_tupleTuple = result.fetchall()
_list = []
for i in range(100):
    _list.append(result.fetchone())

# 关闭连接
connection.close()
cursor.close()
