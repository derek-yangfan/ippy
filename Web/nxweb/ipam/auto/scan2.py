import os,time
import sys
import socket, struct

def ip_to_long(ip_address):
    """
    convert ip to long
    """
    packed_ip = socket.inet_aton(ip_address)
    # 使用0是因为解包的是一个单元素的元组
    return struct.unpack('!L', packed_ip)[0]

#定义文件路径
print("当前路径 -> %s" %os.getcwd())
current_path = os.path.dirname(__file__)

start_Time=int(time.time())
ip_True = open(current_path + '/ip_True.txt','w+')
ip_False = open('ip_False.txt','w+')
IPhost = []
IPbegin = (input(u'请输入起始查询IP： '))
IPend = input(u'请输入终止查询IP： ')
IP1 = IPbegin.split('.')[0]
IP2 = IPbegin.split('.')[1]
IP3 = IPbegin.split('.')[2]
IP4 = IPbegin.split('.')[-1]
IPend_last = IPend.split('.')[-1]
count_True,count_False = 0,0
for i in range(int(IP4)-1,int(IPend_last)):
  ip = str(IP1+'.'+IP2+'.'+IP3+'.'+IP4)
  int_IP4 = int(IP4)
  int_IP4 += 1
  IP4 = str(int_IP4)
  return1=os.system('ping -n 1 -w 1 %s'%ip)
  ip1 = str(ip_to_long(ip))
  if return1:
    print('ping %s is fail'%ip)
    ip_False.write(ip1+'\n')
    count_False += 1
  else:
    print('ping %s is ok'%ip)
    ip_True.write(ip1+'\n')
    count_True += 1
ip_True.close()
ip_False.close()
end_Time = int(time.time())
print("time(秒)：",end_Time - start_Time,"s")
print("ping通的ip数：",count_True,"  ping不通的ip数：",count_False)



