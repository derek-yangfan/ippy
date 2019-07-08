import functions as func


class ip():
    """define IP address class"""

    def __init__(self, address):
        """Initial the IP address and set its init properties"""
        if isinstance(address, str):
            self.address = func.ip_to_long(address)
        else:
            self.address = int(address)

    def get_subnet(self):
        "convert to subnet int"
        subnet1 = func.ip_to_subnet(self.address)
        return func.ip_to_long(subnet1)

    def check_ip(self, cursor):
        "检查IP是否已经存在"
       
        sql = "select * from host where ip = '%s'"%self.address
        cursor.execute(sql)
        result = cursor.fetchone()
        if result == None:
            print('no')
            return False
        else:
            print('yes')
            return True

    def new_ip(self, cursor):
        "新建IP记录"
        sql = """INSERT INTO HOST(HOSTNAME,
                IP, ALIVE, LAST_RESPONSE) 
                VALUES ('new_scan', '%s', 1,  1562296665)"""%self.address
        cursor.execute(sql)
        print("IP: %s is added")%self.address

    def update_ip(self, cursor):
        "更新IP记录"
        sql = "update host set alive = 1 where ip = '%s'" %self.address
        print(sql)
        cursor.execute(sql)  

    def tackle_ip(self, cursor):    #处理IP
        
        if ip.check_ip(self, cursor):
            ip.update_ip(self, cursor)
        else:
            ip.new_ip(self, cursor)
    
    def print_ip(self):
        #打印IP地址信息
        print(self.address)

    