# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:43:41 2024

@author: chana
"""
import time

start_time = time.time()

with open("pi1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์
    
def InsertionSort(a_list):
    n = len(a_list)
    
    for i in range(1,n):
        
        temp = a_list[i]
        hole = i
        
        while hole>0 and a_list[hole-1]<temp:
            a_list[hole] = a_list[hole-1]
            hole = hole-1
            
        a_list[hole] = temp
        
    return a_list

a = InsertionSort(lines)

sorted_lines = InsertionSort(lines)
end_time = time.time()
elapsed_time = end_time - start_time

for line in a:
    print(line.strip())  # ลบ \n ออกเมื่อแสดงผล

print(f"เวลาที่ใช้: {elapsed_time} วินาที")
