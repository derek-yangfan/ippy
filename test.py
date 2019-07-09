import ip
import settings
import functions

IPbegin = (input(u'请输入起始查询IP： '))
ip_obj = ip.ip(IPbegin)
addr1 = ip_obj.address
print(functions.ip_to_subnet(addr1))
print(functions.ip_to_brocast(addr1))
#ip_obj.print_ip()

settings1 = settings.settings()

db = settings1.db_connect()
cursor = db.cursor()

#ip_obj.get_rednum(cursor)
ip_obj.new_ip(cursor)



#ip_obj.check_ip(cursor)

db.commit()
db.close()