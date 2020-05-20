import pymysql
from typing import Dict, List


def convert_dict_to_sql(self, my_dict: Dict) -> List:
    columns = ', '.join("'" + str(x).replace('/', '_') + "'" for x in my_dict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in my_dict.values())

    return [columns, values]


class Database:
    # Open database connection
    DATABASE = pymysql.connect("localhost", "admin", "N0n@me1984", "testing")

    # prepare a cursor object using cursor() method
    cursor = DATABASE.cursor()

    @staticmethod
    def insert(self, table, data):
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (table, Database.convert_dict_to_sql(data)[0], Database.convert_dict_to_sql(data)[1])
        self.cursor.execute(sql)
        self.cursor.commit()
        self.DATABASE.close()



