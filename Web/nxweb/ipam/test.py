import functions as func


db = func.db_connect()
cursor = db.cursor()

print(func.list_subnets(cursor))



