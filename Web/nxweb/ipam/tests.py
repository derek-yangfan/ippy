from django.test import TestCase
import socket, struct

# Create your tests here.

import ipam.functions as func 

print(func.ip_to_long('10.243.16.1'))
