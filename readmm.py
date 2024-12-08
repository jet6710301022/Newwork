import re

# ใช้ with เพื่อเปิดไฟล์
with open("mm.sql", "r", encoding="utf-8") as mm_sql, open("mm.txt", "w", encoding="utf-8") as mm_txt:
    for line in mm_sql:
        # ใช้ regex ดึงเฉพาะข้อมูลใน VALUES(...)
        match = re.search(r"VALUES\s*\((.+)\);", line)
        if match:
            # ดึงค่าที่อยู่ในวงเล็บ VALUES(...)
            values = match.group(1)
            
            # ลบ NULL, , และ ' ออก
            cleaned_values = values.replace("NULL", "").replace("'", "").replace(",", " ").strip()
            
            # เขียนค่าที่ทำความสะอาดแล้วลงไฟล์ .txt
            mm_txt.write(cleaned_values + "\n")
