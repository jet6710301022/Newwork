# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:47:25 2024

@author: chana
"""

# เปิดไฟล์ mm.txt
with open("pi.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์


with open("pi_deta.txt", "w", encoding="utf-8") as output_file:
    
    for line in lines:
        
        if "VALUES" in line:
            # ตัดส่วน VALUES ออก
            values_part = line.split("VALUES")[1]

            
            values_part = values_part.strip(" ();\n").replace("'", "")

            
            values = values_part.split(", ")

            
            mcode = values[0]
            mname = values[1]
            mno = values[2]
            mtype = values[3]
            pcode = values[4]
            pname = values[5]
            acode = values[6]
            aname = values[7]
            tcode = values[8]
            tname = values[9]
            orgname = values[11]
            orgtype = values[12]

            
            output = f"{mcode} {mname}\n"

            
            output_file.write(output)

print("เขียนข้อมูลสำเร็จ!")
