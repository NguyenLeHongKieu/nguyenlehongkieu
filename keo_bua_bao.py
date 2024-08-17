# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:06:52 2024

@author: kieu0
"""

from random import randint
nguoi=int(input('ban vui long chon:1. keo, 2. bua, 3. bao:'))
may=randint(1,3)
if may==1:
    print('may chon keo')
if may==2:
    print('may chon bua')
if may==3:
    print('may chon bao')
if may==nguoi:
    print('------hoa---------')
if may==1 and nguoi==2:
    print('------thang-------')
if may==1 and nguoi==3:
    print('------thua--------')
if may==2 and nguoi==1:
    print('------thua--------')
if may==2 and nguoi==3:
    print('------thang-------')
if may==3 and nguoi==1:
    print('------thang-------')
if may==3 and nguoi==2:
    print('------thua--------')