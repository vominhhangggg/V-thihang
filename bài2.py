# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:54:23 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
m = a + b 
n = a - b
p = a * b
q = a / b
l = a % b
h = a // b
print("Tổng: ", m)
print("Hiệu: ", n)
print("Tích: ", p)
print("Thương: ", q)
print("Thương làm tròn 2 chữ số: ", round(q,2))
print("Thương làm tròn 3 chữ số: ", round(q,3))
print("Chia lấy dư: ", l)
print("Chia lấy nguyên: ", h)