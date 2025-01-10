from function import initialize_file, list_files_in_folder, select_file, add_data, display_data, delete_data, edit_data, search_data
import os
import json
import datetime


# ฟังก์ชันหลัก
def main_menu():
    # เลือกไฟล์
    filename = select_file()

    # สร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
    file_path = initialize_file(filename)

    while True:
        display_data(file_path)

        print("\n--- ระบบจัดการข้อมูล Digital Signage ---")
        print("1. เพิ่มข้อมูล")
        print("2. แสดงข้อมูลทั้งหมด")
        print("3. แก้ไขข้อมูล")
        print("4. ลบข้อมูล")
        print("5. ค้นหาข้อมูล")
        print("6. ออกจากโปรแกรม")
        choice = input("กรุณาเลือกตัวเลือก (1/2/3/4/5/6): ")

        if choice == '1':
            add_data(file_path)
        elif choice == '2':
            display_data(file_path)
        elif choice == '3':
            edit_data(file_path)
        elif choice == '4':
            delete_data(file_path)
        elif choice == '5':
            search_data(file_path)  # เรียกใช้งานฟังก์ชันค้นหา
        elif choice == '6':
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกตัวเลือกที่ถูกต้อง!")
