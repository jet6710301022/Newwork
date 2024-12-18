import os
import re

def bubble_sort(data, key_index=0):
    """
    Bubble Sort สำหรับเรียงข้อมูลในลิสต์
    :param data: ลิสต์ของข้อมูลที่ต้องการเรียง
    :param key_index: อินเด็กซ์ของคอลัมน์ที่จะใช้เป็นคีย์เรียง
    :return: ลิสต์ที่เรียงแล้ว
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key_index] > data[j + 1][key_index]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def process_insert_statements_in_folder(folder_path="."):
    """
    อ่านไฟล์ SQL ทั้งหมดในโฟลเดอร์ที่กำหนด และประมวลผลคำสั่ง INSERT
    :param folder_path: โฟลเดอร์ที่เก็บไฟล์ SQL
    """
    extracted_data = []  # เก็บข้อมูลที่แยกออกมา

    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            # ตรวจสอบว่าเป็นไฟล์ .sql เท่านั้น
            if os.path.isfile(file_path) and file_name.endswith('.sql'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, start=1):
                        line = line.strip()  # ลบช่องว่างและ newline
                        
                        # ใช้ regex เพื่อจับคำสั่ง INSERT ที่ยืดหยุ่นกับชื่อเทเบิลและช่องว่าง
                        match = re.match(r"INSERT INTO\s+`?(\w+)`?\s*\((.*?)\)\s*VALUES\s*\((.*?)\);", line, re.IGNORECASE)
                        
                        if match:
                            table_name = match.group(1)  # ชื่อเทเบิล
                            columns = match.group(2)     # คอลัมน์ในวงเล็บแรก
                            values = match.group(3)      # ค่าข้อมูลในวงเล็บที่สอง

                            # แปลงข้อมูลใน values ให้เป็นลิสต์
                            values_list = [val.strip().strip("'") for val in values.split(',')]

                            # เก็บเฉพาะค่า pcode และ pname ถ้ามี 2 คอลัมน์ขึ้นไป
                            if len(values_list) >= 2:
                                extracted_data.append(values_list)
                        else:
                            print(f"Line {line_number} ในไฟล์ {file_name} ไม่สามารถแยกคำสั่ง INSERT ได้")
    except FileNotFoundError:
        print(f"โฟลเดอร์ '{folder_path}' ไม่พบ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    # เรียงข้อมูลด้วย Bubble Sort โดยใช้คีย์เป็นค่าของคอลัมน์แรก (pcode)
    sorted_data = bubble_sort(extracted_data, key_index=0)

    # แสดงผลข้อมูลที่เรียงแล้ว
    print("\nข้อมูลหลังการจัดเรียง:")
    for record in sorted_data:
        print(f"Pcode: {record[0]}, Pname: {record[1]}")

# เรียกใช้งาน
process_insert_statements_in_folder(".")  # อ่านไฟล์ SQL ในโฟลเดอร์ปัจจุบัน
