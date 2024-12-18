# ฟังก์ชันสำหรับค้นหาข้อมูลในไฟล์
def search_data(file_path, search_key):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            
            if line.startswith(search_key):
                return line.strip()
    return "ไม่พบข้อมูลที่ค้นหา"


file_path = "pi_deta.txt"
search_key = input("Enter The Code:")


result = search_data(file_path, search_key)
print(result)
