import pymysql

conn = pymysql.connect(
    host = "10.243.16.185",
    user = "root",
    password= "Client2db!",
    db = "gestioip",
    port = 3306
    )
cursor = conn.cursor()

"""
sql = "select * from gestioip.host where ip ='183701511'"

cursor.execute(sql)
print (cursor.rownumber)
result = cursor.fetchone()
while result!=None:
        print(result, cursor.rownumber)
        result = cursor.fetchone()


result = cursor.fetchone()
print(result, cursor.rownumber)
result = cursor.fetchone()
print(result, cursor.rownumber)
"""
sql = "update host set alive = 0 where ip = '183701511'"
cursor.execute(sql)

conn.commit()
conn.close()
print('finish')