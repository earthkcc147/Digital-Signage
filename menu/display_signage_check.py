from function import *
import os
import json
import datetime
from colorama import init, Fore, Style, Back

# ฟังก์ชันหลัก
def main_menu():
    # เลือกไฟล์
    filename = select_file()

    # สร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
    file_path = initialize_file(filename)

    while True:
        display_data(file_path)

        # แสดงหัวข้อที่เป็น bold และ bright
        print_header("--- ระบบจัดการข้อมูล Digital Signage ---")
        
        # ใช้ฟังก์ชัน print_menu สำหรับเมนู
        print_menu("1. เพิ่มข้อมูล  📄")
        print_menu("2. แสดงข้อมูลทั้งหมด  📊")
        print_menu("3. แก้ไขข้อมูล  ✏️")
        print_menu("4. ลบข้อมูล  🗑️")
        print_menu("5. ค้นหาข้อมูล  🔍")
        print_menu("6. อธิบายโปรแกรม  📖")
        print_menu("7. ออกจากโปรแกรม  ❌")
        
        # รับค่าจากผู้ใช้
        # choice = colored_input("กรุณาเลือกตัวเลือก (1/2/3/4/5/6): ", Fore.GREEN)
        choice = colored_input("กรุณาเลือกตัวเลือก (1/2/3/4/5/6): ")

        if choice == '1':
            add_data(file_path)
        elif choice == '2':
            display_data(file_path)
        elif choice == '3':
            edit_data(file_path)
        elif choice == '4':
            delete_data(file_path)
        elif choice == '5':
            search_data(file_path)  
        elif choice == '6':
            explain_program()
        elif choice == '7':
            print_alarm("ออกจากโปรแกรม  👋")
            break
        else:
            print_error("กรุณาเลือกตัวเลือกที่ถูกต้อง! " + Style.BRIGHT)