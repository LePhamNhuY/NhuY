# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:51:58 2024

@author: Le Pham Nhu Y
"""
import math
a=float(input("nhập a:"))
b=float(input("nhập b:"))
s=((math.sqrt(a)-math.sqrt(b))/(math.pow(a,0.25)-math.pow(b,0.25)))- ((math.sqrt(a)+math.pow((a*b),0.25))/(math.pow(a,0.25)+math.pow(a,0.25)))
print("kết quả s=",s)
