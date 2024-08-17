# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:12:47 2024

@author: kieu0
"""

try:
    a = float(input("Nhap he so a: "))
    b = float(input("Nhap he so b: "))
    c = float(input("Nhap he so c: "))
except: print("Dinh dang do dai ba canh a, b, c sai!")
if a>0 and b>0 and c>0:
    if a+b>c and b+c>a and a+c>b:
        print('a=',a,'b=',b,'c=',c,"la do dai ba canh cua mot tam giac", sep=(' '))
    else:
        print('a=',a,'b=',b,'c=',c,"khong la do dai ba canh cua mot tam giac", sep=(' '))
else: print("Dinh dang do dai ba canh a, b, c sai!")