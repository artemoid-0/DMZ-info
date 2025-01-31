import pymysql
import subprocess

cmd = ['C', db, '-u', user, '-p', passwd,  '<', '/path/to/script.sql']

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1607',
                             database='warzone_site_db'
                             )

with connection:
    cursor = connection.cursor()

    cursor.execute("INSERT INTO craft_items (item_name, price) VALUES (?, ?)",
                   ('test_item1', '500')
                   )

    rows = cursor.fetchall()
