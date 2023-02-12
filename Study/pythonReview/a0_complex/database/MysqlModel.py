#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/02
# file: MysqlModel.py
# Email:
# Author: rakiwine

import pymysql
import functools

insert_sql = """
INSERT INTO `{}`
    ({})
VALUE
"""


def verify_deal(origin):
    @functools.wraps(origin)
    def inner(*args, **kwargs):

        self = args[0]

        _tableName = kwargs.get("_tableName")
        _keyList = kwargs.get("_keyList")
        _listDict = kwargs.get("_listDict")

        # verify
        if _keyList and not len(_keyList):
            return

        if _keyList and not len(_listDict):
            return

        self.set_connection_cursor()
        res = origin(*args, **kwargs)
        self.del_connection_cursor()

        return res

    return inner


class MysqlModel:

    def __init__(self, username, password, host, database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

        self.connection = None
        self.cursor = None

    def set_connection_cursor(self):
        self.connection = pymysql.connect(user=self.username, password=self.password, host=self.host, db=self.database)
        self.cursor = self.connection.cursor()

        print("MySQL is Connect")

    def del_connection_cursor(self):
        self.cursor.close()
        self.connection.close()

        self.connection = None
        self.cursor = None

        print("MySQL is Closed")

    @verify_deal
    def insert_mysql_by_executemany(self, _tableName, _keyList, _listDict):
        _keyString = ",".join(_keyList)
        sql = insert_sql.format(_tableName, _keyString)

        sql += '    ({})'.format("%s" * len(_keyList))

        _listTuple = []
        for _index, _dict in enumerate(_listDict):
            param = tuple(_dict.values())
            _listTuple.append(param)

        self.cursor.executemany(sql, _listTuple)
        self.connection.commit()

        results = self.cursor.fetchall()
        print(results)

    @verify_deal
    def insert_mysql_by_execute_every(self, _tableName, _keyList, _listDict):
        _keyString = ",".join(_keyList)
        sql = insert_sql.format(_tableName, _keyString)

        sql += '    ({})'.format("%s" * len(_keyList))

        for _index, _dict in enumerate(_listDict):
            param = tuple(_dict.values())
            self.cursor.execute(sql, param)

        self.connection.commit()

        results = self.cursor.fetchall()
        print(results)

    @verify_deal
    def insert_mysql_by_execute_once(self, _tableName, _keyList, _listDict):
        _keyString = ",".join(_keyList)
        sql = insert_sql.format(_tableName, _keyString)

        for _index, _dict in enumerate(_listDict):
            if _index > 0:
                sql += ",\n"
            _valueList = []
            for _key in _keyList:
                _valueList.append(str(_dict[_key]))

            _valueString = '","'.join(_valueList)
            sql += '    ("{}")'.format(_valueString)

        # print(sql)


        self.connection.commit()

        results = self.cursor.fetchall()
        print(results)

    @verify_deal
    def select_mysql(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()

        return results


if __name__ == "__main__":
    _username = "root"
    _password = "Root_123"

    _host = "127.0.0.1"
    _database = "poker"

    try:
        mysql = MysqlModel(_username, _password, _host, _database)
        listDict = [
            {'id': 4719036405061259749, 'name': '藩风', 'isAI': 1},
            {'id': 4719036405069647891, 'name': '留孤莲', 'isAI': 1},
            {'id': 4719036405078036476, 'name': '国锦墨', 'isAI': 1}
        ]
        mysql.insert_mysql_by_execute_once(_tableName="User", _keyList=["id", "name", "isAI"], _listDict=listDict)
    except pymysql.err.ProgrammingError as e:
        print("Exception Error is %s" % e)
    except pymysql.err.OperationalError as e:
        print("Exception Error is %s" % e)
