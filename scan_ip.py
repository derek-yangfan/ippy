import os,time
import sys
import socket, struct
import ip
import settings
import functions as func


#定义文件路径
print("当前路径 -> %s" %os.getcwd())
current_path = os.path.dirname(__file__)

start_Time=int(time.time())
ip_True = open(current_path + '/ip_True.txt','w+')
ip_False = open(current_path + '/ip_False.txt','w+')


#IPhost = []
#IPbegin = (input(u'请输入起始查询IP： '))
#IPend = input(u'请输入终止查询IP： ')

#IP1 = IPbegin.split('.')[0]
#IP2 = IPbegin.split('.')[1]
#IP3 = IPbegin.split('.')[2]
#IP4 = IPbegin.split('.')[-1]
#IPend_last = IPend.split('.')[-1]

ip_start = func.ip_to_long(input(u'请输入起始查询IP： '))
ip_end = func.ip_to_long(input(u'请输入终止查询IP： '))

count_True,count_False = 0,0

for ip in range(ip_start, ip_end):
  ip = func.long_to_ip(ip)
  return1=os.system('ping -n 1 -w 1 %s'%ip)

  #IP转换成数字
  #ip1 = str(func.ip_to_long(ip))
  if return1:
    #print('ping %s is fail'%ip)
    ip_False.write(ip+'\n')
    count_False += 1
  else:
    #print('ping %s is ok'%ip)
    ip_True.write(ip+'\n')
    count_True += 1
ip_True.close()
ip_False.close()
end_Time = int(time.time())
print("time(秒)：",end_Time - start_Time,"s")
print("ping通的ip数：",count_True,"  ping不通的ip数：",count_False)



