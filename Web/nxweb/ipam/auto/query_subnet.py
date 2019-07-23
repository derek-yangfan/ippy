import socket, struct
import os
import pymysql
import ip
import settings
import functions as func

def get_subnets(cursor,site, line, cell):
        "检查IP是否已经存在"
       
        sql = """select red, bm, descr, locations.loc as site, categoria, comentario, Line, Cell, client_id from 
            (select red, bm, descr, loc, categoria, comentario, max(if(cc_id = '2', entry, 0)) 'Line', max(if(cc_id = '3', entry, 0)) 'Cell'
            from custom_net_column_entries as a 
            left join net on a.net_id = net.red_num 
            group by net_id) as b 
            left join locations on b.loc = locations.id where locations.loc ='%s' and line = '%s' and find_in_set('%s', cell);"""%(site, line, cell)

        cursor.execute(sql)
        result = cursor.fetchall()
        for r1 in result:
            if result == None:
                print('no')
            
            else:
                return r1[0]
            

if __name__ == "__main__":
    """系统自动分配输入网段的IP段"""

    """input IP address"""
    i_site = (input(u'请输入Plant (例如Plant 51)： '))
    i_line= (input(u'请输入Line： '))
    i_cell = (input(u'请输入Cell： '))


    """Initial connection to DB"""
    settings1 = settings.settings()
    db = settings1.db_connect()
    cursor = db.cursor()


    get_subnets(cursor, i_site, i_line, i_cell)


    db.close()

