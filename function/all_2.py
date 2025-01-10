import os
import json
import datetime


FOLDER_NAME = 'check'


# ฟังก์ชันตรวจสอบและสร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
def initialize_file(filename):
    # ตรวจสอบและสร้างโฟลเดอร์ถ้ายังไม่มี
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print(f"สร้างโฟลเดอร์ {FOLDER_NAME} เรียบร้อยแล้ว")

    # สร้างไฟล์ในโฟลเดอร์ถ้ายังไม่มี
    file_path = os.path.join(FOLDER_NAME, filename)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)  # สร้างไฟล์พร้อมข้อมูลว่าง
        print(f"สร้างไฟล์ {file_path} เรียบร้อยแล้ว")
    else:
        print(f"ไฟล์ {file_path} มีอยู่แล้ว ไม่ต้องสร้างใหม่")

    return file_path


# ฟังก์ชันแสดงรายชื่อไฟล์ในโฟลเดอร์ check
def list_files_in_folder():
    # ตรวจสอบและสร้างโฟลเดอร์ 'check' ถ้ายังไม่มี
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print(f"สร้างโฟลเดอร์ {FOLDER_NAME} เรียบร้อยแล้ว")

    print("\n--- ไฟล์ที่มีอยู่ในโฟลเดอร์ 'check' ---")
    files = os.listdir(FOLDER_NAME)
    if files:
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")
    else:
        print("ยังไม่มีไฟล์ในโฟลเดอร์")