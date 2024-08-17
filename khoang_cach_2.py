# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:41:53 2024

@author: kieu0
"""

distance = float(input("Nhap do dai doan duong den truong (m): "))

if distance < 300:
    print("Duong den truong qua gan. Thoi! Di bo")
elif distance > 1200:
    print("Duong den truong qua xa. Thoi! Di xe may")
elif distance >= 300 and distance <=700:
    print("Duong den truong khong xa. Thoi! Di xa dap")
else:
    print("Khong xac dinh")
    