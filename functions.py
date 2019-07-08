import socket, struct

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
  

