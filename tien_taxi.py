# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:49:35 2024

@author: kieu0
"""

km = float(input("Nhap so km: "))
if km <= 1:
    fare = 20
elif km <= 3:
    fare = 20 + (km - 1) * 13
elif km <= 8:
    fare = 20 + 2 * 13 + (km -3) * 12
else:
    fare = 20 + 2 * 13 + 5 * 12 + (km - 8) * 10
if fare >100:
    fare *= 0.92 # giam 8%
print(f"Tong tien: {fare}k")