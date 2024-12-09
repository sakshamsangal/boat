import json
import time

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="world"
)
cursor = connection.cursor()
# query = f"SELECT * FROM city where name='Kabul' limit 100"
# cursor.execute(query)
# users = cursor.fetchall()
# print(users)

with open("../static/tables.json") as json_file:
    data = json.load(json_file)


def outside_loop():
    for tb in data["tbs"]:
        x = tb['cols'].keys()
        y = [*tb['cols'].values()]
        vals = ", ".join(['%s'] * len(x))
        sql = f"INSERT INTO {tb['name']} ({', '.join(x)}) VALUES({vals});"
        try:
            cursor.execute(sql, y)
            connection.commit()
            print(tb['name'], "entry created")
        except Exception as e:
            connection.rollback()
            print(e)
    # try:
    # except Exception as e:
    #     print("Failure..", e)


outside_loop()
connection.close()
