import socket, struct
import os
import pymysql
import ip
import settings
import functions as func


if __name__ == "__main__":
    """系统自动分配输入网段的IP地址"""

    """Initial connection to DB"""
    settings1 = settings.settings()
    db = settings1.db_connect()
    cursor = db.cursor()

    """input IP address"""
    IPbegin = (input(u'请输入起始查询IP： '))
    ip_obj = ip.ip(IPbegin)
    addr1 = ip_obj.address
    subnet_int = ip_obj.get_subnet()


    count = int(input(u'请输入你需要IP的数量： '))

    for s1 in range(subnet_int+1, subnet_int+100):
        if count >=1:
            if not func.query_ip(s1, cursor):
                print(func.long_to_ip(s1) + ' is available to use')
                count -=1
            #else:
                #print(func.long_to_ip(s1) + ' is not available to use')
        else:
            break

    db.close()