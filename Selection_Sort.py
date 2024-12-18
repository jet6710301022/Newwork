# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:15:17 2024

@author: chana
"""
import time

start_time = time.time()

with open("pi_deta.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

def SelectionSort(a_list):
    n = len(a_list)

    for i in range(0, n-1):
        iMin = i

        for j in range(i+1, n):
            
            if a_list[j] > a_list[iMin]:
                iMin = j

        # สลับตำแหน่ง
        temp = a_list[i]
        a_list[i] = a_list[iMin]
        a_list[iMin] = temp

    return a_list

# เรียงลำดับข้อมูล
sorted_lines = SelectionSort(lines)

end_time = time.time()
elapsed_time = end_time - start_time



# แสดงข้อมูลที่เรียงแล้ว
for line in sorted_lines:
    print(line.strip())  # ลบ \n ออกเมื่อแสดงผล

print(f"เวลาที่ใช้: {elapsed_time:.2f} วินาที")
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"เวลาที่ใช้ในการประมวลผล: {elapsed_time:.2f} วินาที")


