from function import initialize_file, list_files_in_folder, select_file, add_data, display_data, delete_data, edit_data, search_data, explain_program
import os
import json
import datetime
from colorama import init, Fore, Style, Back

# เริ่มต้น colorama
init(autoreset=True)

# ฟังก์ชันหลัก
def main_menu():

    # เลือกไฟล์
    filename = select_file()

    # สร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
    file_path = initialize_file(filename)

    while True:
        display_data(file_path)

        # แสดงหัวข้อที่เป็น bold และ bright
        # print(Fore.YELLOW + "\033[1m" + Style.BRIGHT + "--- ระบบจัดการข้อมูล Digital Signage ---" + "\033[0m")
        # แสดงหัวข้อที่เป็น bold และ bright
        print(Fore.YELLOW + "\033[1m" + "--- ระบบจัดการข้อมูล Digital Signage ---" + "\033[0m")
        print(Fore.CYAN + "1." + Style.BRIGHT + " เพิ่มข้อมูล  📄")
        print(Fore.CYAN + "2." + Style.BRIGHT + " แสดงข้อมูลทั้งหมด  📊")
        print(Fore.CYAN + "3." + Style.BRIGHT + " แก้ไขข้อมูล  ✏️")
        print(Fore.CYAN + "4." + Style.BRIGHT + " ลบข้อมูล  🗑️")
        print(Fore.CYAN + "5." + Style.BRIGHT + " ค้นหาข้อมูล  🔍")
        print(Fore.CYAN + "6." + Style.BRIGHT + " อธิบายโปรแกรม  📖")
        print(Fore.RED + "7." + Style.BRIGHT + " ออกจากโปรแกรม  ❌")
        
        choice = input(Fore.GREEN + "กรุณาเลือกตัวเลือก (1/2/3/4/5/6): ")

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
            print(Fore.YELLOW + "ออกจากโปรแกรม  👋")
            break
        else:
            print(Fore.RED + "กรุณาเลือกตัวเลือกที่ถูกต้อง! " + Style.BRIGHT)