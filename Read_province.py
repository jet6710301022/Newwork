# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:47:25 2024

@author: chana
"""
# เปิดไฟล์ province.txt
with open("province.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์

# เปิดไฟล์ test1.txt สำหรับเขียนข้อมูล
with open("test1.txt", "w", encoding="utf-8") as output_file:
    # วนลูปผ่านแต่ละบรรทัด
    for line in lines:
        # ตรวจสอบว่ามีคำว่า VALUES ในแต่ละบรรทัด
        if "VALUES" in line:
            # ตัดส่วน VALUES ออก
            values_part = line.split("VALUES")[1]
            
            # ลบเครื่องหมายวงเล็บ, ช่องว่าง, และ ;
            values_part = values_part.strip(" ();")
            
            # แยกค่าด้วยเครื่องหมายคอมมา
            values = values_part.split(", ")
            
            # ดึงค่า pcode และ pname
            pcode = values[0]  # ค่าแรก
            pname = values[1].strip("'")  # ค่าที่สอง (ลบเครื่องหมาย ')
            
            # แสดงผลลัพธ์
            print(f"{pcode} {pname}")
            
            # เขียนข้อมูลลงไฟล์ test1.txt
            output_file.write(f"{pcode} {pname}\n")

print("เขียนข้อมูลสำเร็จ!")
