import os
import json
import datetime
from openpyxl import Workbook


EXEL_FOLDER_NAME = 'exel'  # โฟลเดอร์ที่จะบันทึกไฟล์ .xlsx

# ฟังก์ชันแปลงไฟล์ JSON เป็นไฟล์ .xlsx
def convert_to_xlsx():
    # ตรวจสอบและสร้างโฟลเดอร์ 'exel' ถ้ายังไม่มี
    if not os.path.exists(EXEL_FOLDER_NAME):
        os.makedirs(EXEL_FOLDER_NAME)
        print(f"สร้างโฟลเดอร์ {EXEL_FOLDER_NAME} เรียบร้อยแล้ว")

    # แสดงไฟล์ในโฟลเดอร์ check
    files = list_files_in_folder()

    # หากไม่มีไฟล์ในโฟลเดอร์
    if not files:
        return

    # ขอให้ผู้ใช้เลือกไฟล์จากหมายเลข
    try:
        choice = int(input("กรุณาเลือกหมายเลขไฟล์ที่ต้องการแปลง (หรือกรอก 0 เพื่อออก): "))
        if choice == 0:
            print("ออกจากโปรแกรม")
            return
        if choice < 1 or choice > len(files):
            print("เลือกหมายเลขไฟล์ไม่ถูกต้อง")
            return
    except ValueError:
        print("กรุณากรอกหมายเลขที่ถูกต้อง")
        return

    json_filename = files[choice - 1]
    json_file_path = os.path.join(FOLDER_NAME, json_filename)

    # ตรวจสอบว่าไฟล์ JSON มีอยู่หรือไม่
    if not os.path.exists(json_file_path):
        print(f"ไม่พบไฟล์ {json_filename} ในโฟลเดอร์ {FOLDER_NAME}")
        return

    # อ่านข้อมูลจากไฟล์ JSON
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # สร้างไฟล์ Excel (.xlsx)
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"

    # หากข้อมูลมี ให้เพิ่มชื่อคอลัมน์
    if data:
        headers = list(data[0].keys())  # หัวข้อของแต่ละคอลัมน์จากข้อมูลใน JSON
        ws.append(headers)

        # เพิ่มข้อมูลในแต่ละแถว
        for row in data:
            ws.append(list(row.values()))

    # กำหนดชื่อไฟล์ .xlsx
    xlsx_filename = json_filename.replace('.json', '.xlsx')
    xlsx_file_path = os.path.join(EXEL_FOLDER_NAME, xlsx_filename)  # บันทึกในโฟลเดอร์ 'exel'

    # บันทึกไฟล์ .xlsx
    wb.save(xlsx_file_path)
    print(f"แปลงไฟล์ {json_filename} เป็นไฟล์ .xlsx เรียบร้อยแล้ว: {xlsx_filename}")


# เรียกฟังก์ชันแปลงไฟล์ JSON เป็นไฟล์ .xlsx
convert_to_xlsx()