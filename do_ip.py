import os
import pymysql

def exec_sql(self, cursor):
    "connect to mysql and execute sql"
    cursor.execute(self)
    

def check_ip(self, cursor):
    "检查IP是否已经存在"
    sql = "select * from host where ip = '%s'"%self
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        print('no')
        return False
    else:
        print('yes')
        return True

def new_ip(self, cursor):
    "新建IP记录"
    sql = """INSERT INTO HOST(HOSTNAME,
             IP, ALIVE, LAST_RESPONSE) 
            VALUES ('new_scan', '%s', 1,  1562296665)"""%self
    exec_sql(sql,cursor)

def update_ip(self, cursor):
    "更新IP记录"
    sql = "update host set alive = 1 where ip = '%s'" %self
    print(sql)
    exec_sql(sql, cursor)   

def do_ip(self, cursor):
    "处理IP"
    if check_ip(self, cursor):
        update_ip(self, cursor)
    else:
        new_ip(self, cursor)


    
if __name__ == "__main__":
    #定义文件路径
    print("当前路径 -> %s" %os.getcwd())
    current_path = os.path.dirname(__file__)

    #建立mysql连接   
    db = pymysql.connect("10.243.16.185","root","Client2db!","gestioip")
    cursor = db.cursor()

    #读取txt文件行
    f = open(current_path + "/1.txt")
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        do_ip(line, cursor)

    f.close
    db.commit()
    db.close()





