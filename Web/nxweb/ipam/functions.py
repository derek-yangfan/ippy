import socket, struct
import pymysql

def long_to_ip(long_int):
    """
    convert long to ip
    """
    packed_ip = struct.pack('!L', long_int)
    return socket.inet_ntoa(packed_ip)

def ip_to_long(ip_address):
    """
    convert ip to long
    """
    packed_ip = socket.inet_aton(ip_address)
    # 使用0是因为解包的是一个单元素的元组
    return struct.unpack('!L', packed_ip)[0]

def ip_to_subnet(ip):
    """convert ip to its subnet"""
    if isinstance(ip, int):
        ip = long_to_ip(ip)
    ip1 = ip.split('.')[0]
    ip2 = ip.split('.')[1]
    ip3 = ip.split('.')[2]
    subnet = ip1 + '.' + ip2 + '.' + ip3 + '.0'
    return subnet

def ip_to_brocast(ip):
    """get brocast of ip subnet"""
    subnet = ip_to_subnet(ip)
    subnet_int = ip_to_long(subnet) 
    brocast_int = subnet_int + 255
    brocast = long_to_ip(brocast_int)
    return brocast


def query_ip(ip_address, cursor):
        "检查IP是否已经存在"
       
        sql = "select * from host where ip = '%s'"%ip_address
        cursor.execute(sql)
        result = cursor.fetchone()
        if result == None:
            #print('no')
            return False
        else:
            #print('yes')
            return True
  
def assign_subnets(cursor, site, line, cell):
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

def list_subnets(cursor):
    #查询网段
    sql = """select red, bm, net_id, site, categorias_net.cat as line, comentario, descr, client_id  from
            (select red, bm, descr, locations.loc as site, categoria, comentario, client_id, net_id from 
            (select red, bm, descr, loc, categoria, comentario, max(if(cc_id = '2', entry, 0)) 'Line', max(if(cc_id = '3', entry, 0)) 'Cell', net_id
            from custom_net_column_entries as a 
            left join net on a.net_id = net.red_num 
            group by net_id) as b left join locations on b.loc = locations.id) as c 
            left join categorias_net on c.categoria = categorias_net.id """
    cursor.execute(sql)

    result = cursor.fetchall()
    rs = []
    for r1 in result:
        if result == None:
            print('no')
        
        else:
            rs.append(r1)
    return rs

def list_site(cursor):
    #查询网段
    sql = """select distinct site from
            (select red, bm, descr, locations.loc as site, categoria, comentario, client_id, net_id from 
            (select red, bm, descr, loc, categoria, comentario, max(if(cc_id = '2', entry, 0)) 'Line', max(if(cc_id = '3', entry, 0)) 'Cell', net_id
            from custom_net_column_entries as a 
            left join net on a.net_id = net.red_num 
            group by net_id) as b left join locations on b.loc = locations.id) as c 
            left join categorias_net on c.categoria = categorias_net.id """
    cursor.execute(sql)

    result = cursor.fetchall()
    rs = []
    for r1 in result:
        if result == None:
            print('no')
        
        else:
            rs.append(r1)
    return rs
    


def db_connect():
        #Define db information
        hostname = "127.0.0.1"
        username = "root"
        password = "root"
        dbname = "gestioip"
        return pymysql.connect(hostname, username, password, dbname)