import pymysql

class settings():
    "实例化一个DB连接对象"
    def __init__(self):
        #Define db information
        self.hostname = "10.243.16.101"
        self.username = "root"
        self.password = "Client2db!"
        self.dbname = "gestioip"

    def db_connect(self):
        return pymysql.connect(self.hostname, self.username, self.password, self.dbname)


