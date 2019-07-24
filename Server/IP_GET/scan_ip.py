import os,time
import sys
import socket, struct
import functions as func

IPbegin = (input(u'请输入起始查询IP： '))
IPend = input(u'请输入终止查询IP： ')
ip_start = func.ip_to_long(IPbegin)
ip_end = func.ip_to_long(IPend)
ip_subnet = func.ip_to_subnet(IPbegin)

#定义文件路径
print("当前路径 -> %s" %os.getcwd())
current_path = os.path.dirname(__file__)

#打开TXT文件记录ping结果

ip_True = open(current_path + '/files/ip_True_%s.txt'%ip_subnet,'w+')
ip_False = open(current_path + '/files/ip_False_%s.txt'%ip_subnet,'w+')
count_True,count_False = 0,0

start_Time=int(time.time())


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



