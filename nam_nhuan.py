# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:00:34 2024

@author: kieu0
"""

import calendar 
year = int(input("Nhap nam: "))
is_leap = calendar.isleap(year)
print(f"{year} la nam nhuan " if is_leap else f"{year} khong phai la nam nhuan")