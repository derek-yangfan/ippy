import socket, struct
import os
import pymysql
import ip
import settings
import functions as func


if __name__ == "__main__":
    """系统自动分配输入网段的IP地址"""

    """input IP address"""
    i_site = (input(u'请输入Plant (例如Plant 51)： '))
    i_line= (input(u'请输入Line： '))
    i_cell = (input(u'请输入Cell： '))
    count = int(input(u'请输入你需要IP的数量： '))


    """Initial connection to DB"""
    settings1 = settings.settings()
    db = settings1.db_connect()
    cursor = db.cursor()

    subnet = func.assign_subnets(cursor, i_site, i_line, i_cell)
    subnet_int = func.ip_to_long(subnet)

    for s1 in range(subnet_int+1, subnet_int+255):
        if count >=1:
            if not func.query_ip(s1, cursor):
                print(func.long_to_ip(s1) + ' is available to use')
                count -=1
            #else:
                #print(func.long_to_ip(s1) + ' is not available to use')
        else:
            break

    db.close()