# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:16:21 2024

@author: kieu0
"""

a = float(input("Nhap a: "))
b = float(input("Nhao b: "))
if a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem")
elif a == 0 and b != 0:
    print("Phuong trinh vo nghiem")
elif a != 0 and b != 0:
    print("Phuong trinh co 1 nghiem duy nhat X=", -b/a)
else:
    print("Khong hop le!")