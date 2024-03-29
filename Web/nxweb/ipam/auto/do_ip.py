import os
import pymysql
import ip
import functions
import settings


    
if __name__ == "__main__":
    #定义文件路径
    print("当前路径 -> %s" %os.getcwd())
    current_path = 'z:/ip/'

    """Initial connection to DB"""
    settings1 = settings.settings()
    db = settings1.db_connect()
    cursor = db.cursor()
    
    #ip_obj = ip.ip("10.243.40.30")

    #ip_obj.tackle_ip(cursor)

    for filename in os.listdir(current_path):
        if 'alive' in filename:
            print(filename)

            #读取txt文件行
            f = open(current_path + filename)
            lines = f.readlines()
            for line in lines:
                line = line.strip("\n")
                ip_obj = ip.ip(line)
                ip_obj.tackle_ip(cursor)

            f.close
  
    db.commit()
    db.close()





