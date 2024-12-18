# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:35:01 2024

@author: chana
"""


input_file = "pi_deta.txt"
output_file = "sorted_pi.txt"

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()


sorted_lines = sorted(lines, key=lambda x: int(x.split()[0]), reverse=True)


with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(sorted_lines)

print(f"ข้อมูลถูกจัดเรียงและบันทึกในไฟล์ '{output_file}' เรียบร้อย")
