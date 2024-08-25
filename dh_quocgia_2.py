# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:56:04 2024

@author: Le Pham Nhu Y
"""
dia_chi="Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM"
s= dia_chi.replace("P.","").replace("Q.","").replace("Tp.","")
s1= s.split(", ")
for a in s1:
    print(a)
