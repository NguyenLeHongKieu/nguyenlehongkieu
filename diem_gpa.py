# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:43:04 2024

@author: kieu0
"""

GPA = float(input("Nhap diem trung binh GPA: "))
if GPA < 3.5:
    print("Hoc luc kem")
elif 3.5 <= GPA < 5.0:
    print("Hoc luc yeu")
elif 5.0 <= GPA < 7.0:
    print("Hoc luc trung binh")
elif 7.0 <= GPA < 8.0:
    print("Hoc luc kha")
elif 8.0 <= GPA < 9.0:
    print("Hoc luc gioi")
elif 9.0 <= GPA <= 10:
    print("Hoc luc xuat sac")