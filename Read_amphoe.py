# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:47:25 2024

@author: chana
"""

# เปิดไฟล์ amphoe.txt
with open("amphoe.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์

# เปิดไฟล์ amphoe_deta.txt สำหรับเขียนข้อมูล
with open("amphoe_deta.txt", "w", encoding="utf-8") as output_file:
    # วนลูปผ่านแต่ละบรรทัด
    for line in lines:
        # ตรวจสอบว่ามีคำว่า VALUES ในแต่ละบรรทัด
        if "VALUES" in line:
            # ตัดส่วน VALUES ออก
            values_part = line.split("VALUES")[1]
            
            # ลบเครื่องหมายวงเล็บ, ช่องว่าง, และ ;
            values_part = values_part.strip(" ();").replace("');", "").replace("(", "").replace(")", "").strip()
            
            # แยกค่าด้วยเครื่องหมายคอมมา
            values = values_part.split(", ")
            
            # ดึงค่า acode, aname, pcode และ pname
            acode = values[0]  # ค่าแรก
            aname = values[1].strip("'")  # ค่าที่สอง (ลบเครื่องหมาย ')
            pcode = values[2]
            pname = values[3].strip("'")  # ลบเครื่องหมาย '

            # แสดงผลลัพธ์
            print(f"{acode} {aname} {pcode} {pname}")
            
            # เขียนข้อมูลลงไฟล์ amphoe_deta.txt
            output_file.write(f"{acode} {aname} {pcode} {pname}\n")

print("เขียนข้อมูลสำเร็จ!")
