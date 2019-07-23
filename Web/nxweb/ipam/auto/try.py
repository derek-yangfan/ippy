import os
import string

print("当前路径 -> %s" %os.getcwd())
current_path = os.path.dirname(__file__)

for filename in os.listdir(current_path+"/files/"):
    if 'ip_True' in filename:
        print(filename)