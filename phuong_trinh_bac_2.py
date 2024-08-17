# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:35:05 2024

@author: kieu0
"""

import math
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phuong trinh co nghiem kep x = {x}",x)
else:
    x1 = -b +math.sqrt(delta) / (2*a)
    x2 = -b -math.sqrt(delta) / (2*a)
    print(f"Phuong trinh co hai nghiem phan biet x1 = {x1}, x2 = {x2}")
    print("x1:",x1)
    print("x2:",x2)
    

