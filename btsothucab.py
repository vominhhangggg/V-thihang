# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:57:31 2024

@author: ADMIN
"""
import math 
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
tử1=math.sqrt(a)-math.sqrt(b)
mẫu1=a**(1/4)-b**(1/4)
tử2=math.sqrt(a)+(a*b)**(1/4)
mẫu2=a**(1/4)+b**(1/4)
ketqua=(tử1/mẫu1)-(tử2/mẫu2)
print("ket qua cua bieu thuc la:", ketqua)