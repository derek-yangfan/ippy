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
    
    def get_rednum(self,cursor):
        "get rednum for IP address"
        subnet_str = func.ip_to_subnet(self.address)
        sql = "select red_num from net where red = '%s'"%subnet_str
        cursor.execute(sql)
        result = cursor.fetchone()
        red_num = str(result[0])
        return red_num

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
        ip_addr = str(self.address)
        ip_str = func.long_to_ip(self.address)
        red_num = ip.get_rednum(self,cursor)
        sql = """INSERT INTO `host` (`ip`, `hostname`, 
            `loc`, `red_num`, `categoria`, `int_admin`, `update_type`, `alive`, `range_id`, `ip_version`, `client_id`) 
             VALUES ('%s', 'new_scan', '1', '%s', '1', 'n', '3', '1', '-1', 'v4', '1')"""%(ip_addr, red_num)
        cursor.execute(sql)
        print("IP: %s is added"%ip_str)

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

    