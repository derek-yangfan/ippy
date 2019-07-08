# python写法
import socket, struct

def ip_to_long(ip_address):
    """
    convert ip to long
    """
    packed_ip = socket.inet_aton(ip_address)
    # 使用0是因为解包的是一个单元素的元组
    return struct.unpack('!L', packed_ip)[0]
#sss33ss22222222222

ip1 = ip_to_long('10.243.16.1')
print (ip1)