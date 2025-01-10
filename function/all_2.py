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




# ฟังก์ชันให้ผู้ใช้เลือกไฟล์
def select_file():
    try:
        list_files_in_folder()

        while True:
            file_choice = input("กรุณาเลือกหมายเลขไฟล์ หรือกรอกชื่อไฟล์ใหม่: ").strip()

            # ตรวจสอบว่าเป็นหมายเลข
            if file_choice.isdigit():
                file_choice = int(file_choice)
                files = os.listdir(FOLDER_NAME)
                if 1 <= file_choice <= len(files):
                    return files[file_choice - 1]
                else:
                    print("กรุณาเลือกหมายเลขไฟล์ที่ถูกต้อง.")
            else:
                # ตรวจสอบชื่อไฟล์ไม่ให้ว่างเปล่า
                if not file_choice:
                    print("ชื่อไฟล์ไม่สามารถว่างเปล่าได้ กรุณากรอกชื่อไฟล์ใหม่.")
                    continue

                # ตรวจสอบว่าไฟล์มีนามสกุล
                if '.' not in file_choice:
                    print("ชื่อไฟล์ต้องมีนามสกุล เช่น .txt, .json เป็นต้น กรุณากรอกใหม่.")
                    continue

                filename = file_choice
                file_path = os.path.join(FOLDER_NAME, filename)

                # ตรวจสอบว่าไฟล์มีอยู่แล้วหรือไม่
                if os.path.exists(file_path):
                    print(f"ไฟล์ {filename} มีอยู่แล้ว ไม่ต้องสร้างใหม่.")
                    return filename
                else:
                    print(f"ไฟล์ {filename} ไม่มีในโฟลเดอร์ 'check'. สร้างไฟล์ใหม่...")
                    return filename

    except FileNotFoundError:
        print(f"ไม่พบโฟลเดอร์ '{FOLDER_NAME}' กรุณาตรวจสอบโฟลเดอร์อีกครั้ง.")
    except PermissionError:
        print("ไม่สามารถเข้าถึงโฟลเดอร์หรือไฟล์ได้ กรุณาตรวจสอบสิทธิ์การเข้าถึง.")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")





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





# ฟังก์ชันแสดงข้อมูลทั้งหมด
def display_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if data:
                print("\n{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
                    "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
                ))
                print("-" * 100)
                for entry in data:
                    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
                        entry["ลำดับ"],
                        entry["รายการ"],
                        entry["s/n"],
                        entry["อาการ"],
                        entry["ขนาดจอ"],
                        entry["วันที่และเวลาที่ตรวจ"]
                    ))
            else:
                print("ยังไม่มีข้อมูลในระบบ")
    else:
        print("ยังไม่มีข้อมูลในระบบ")






# ฟังก์ชันเพิ่มข้อมูลใหม่
def add_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # กำหนดลำดับอัตโนมัติ
    sequence = len(data) + 1

    # รับข้อมูลจากผู้ใช้ (ตรวจสอบให้ "รายการ" และ "s/n" ไม่ว่าง)
    while True:
        item = input("กรุณาใส่รายการ: ").strip()
        if not item:
            print("กรุณาใส่รายการ ไม่สามารถปล่อยว่างได้!")
        else:
            break

    while True:
        serial_number = input("กรุณาใส่ s/n: ").strip()
        if not serial_number:
            print("กรุณาใส่ s/n ไม่สามารถปล่อยว่างได้!")
        else:
            break

    # รับข้อมูลอาการ (ให้เลือกจาก y, n หรือกรอกเอง)
    while True:
        symptom_choice = input("กรุณาเลือกอาการจอ (y = จอปกติ, n = ไม่ระบุ, หรือกรอกเอง): ").strip().lower()
        
        if symptom_choice == 'y':
            symptom = "จอปกติดี"
            break
        elif symptom_choice == 'n':
            symptom = "ไม่ระบุ"
            break
        elif symptom_choice:
            symptom = symptom_choice  # ถ้ากรอกเอง
            break
        else:
            print("กรุณาเลือกอาการที่ถูกต้อง!")

    # รับข้อมูลขนาดจอ (เลือก n สำหรับ 'ไม่ระบุ')
    while True:
        screen_size = input("กรุณาใส่ขนาดจอ (ถ้าไม่ระบุให้ใส่ n): ").strip().lower()
        
        if screen_size == 'n':
            screen_size = "ไม่ระบุ"
            break
        elif screen_size:
            break  # ถ้ามีการกรอกขนาดจอเอง
        else:
            print("กรุณาใส่ขนาดจอหรือเลือก 'n' สำหรับไม่ระบุ!")

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # เพิ่มข้อมูลใหม่
    new_entry = {
        "ลำดับ": sequence,
        "รายการ": item,
        "s/n": serial_number,
        "อาการ": symptom,
        "ขนาดจอ": screen_size,
        "วันที่และเวลาที่ตรวจ": timestamp
    }
    data.append(new_entry)

    # บันทึกข้อมูลลงไฟล์ JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("บันทึกข้อมูลสำเร็จ!")





# ฟังก์ชันแก้ไขข้อมูล
def edit_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # ถ้าไม่มีข้อมูลในไฟล์
    if not data:
        print("ไม่มีข้อมูลในระบบสำหรับการแก้ไข!")
        return

    # แสดงข้อมูลที่มีอยู่
    print("\n--- ข้อมูลที่มีอยู่ ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 100)
    for entry in data:
        print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
            entry["ลำดับ"],
            entry["รายการ"],
            entry["s/n"],
            entry["อาการ"],
            entry["ขนาดจอ"],
            entry["วันที่และเวลาที่ตรวจ"]
        ))

    # เลือกข้อมูลที่ต้องการแก้ไข
    while True:
        try:
            edit_index = int(input("\nกรุณาเลือกหมายเลขลำดับที่ต้องการแก้ไข (กรอก 00 เพื่อยกเลิก): "))

            # หากกรอก 00 ให้ยกเลิกการแก้ไข
            if edit_index == 00:
                print("ยกเลิกการแก้ไขข้อมูล.")
                return

            # ตรวจสอบว่าหมายเลขลำดับที่เลือกมีอยู่
            entry = next((entry for entry in data if entry["ลำดับ"] == edit_index), None)
            if entry:
                break
            else:
                print("หมายเลขลำดับไม่ถูกต้อง กรุณากรอกใหม่!")
        except ValueError:
            print("กรุณากรอกหมายเลขลำดับที่ถูกต้อง!")

    # แสดงข้อมูลก่อนการแก้ไข
    print(f"\n--- ข้อมูลก่อนการแก้ไข ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 100)
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        entry["ลำดับ"],
        entry["รายการ"],
        entry["s/n"],
        entry["อาการ"],
        entry["ขนาดจอ"],
        entry["วันที่และเวลาที่ตรวจ"]
    ))

    # แก้ไขข้อมูล
    item = input(f"กรุณาใส่รายการใหม่ (ปัจจุบัน: {entry['รายการ']}): ").strip()
    serial_number = input(f"กรุณาใส่ s/n ใหม่ (ปัจจุบัน: {entry['s/n']}): ").strip()
    symptom = input(f"กรุณาใส่อาการใหม่ (ปัจจุบัน: {entry['อาการ']}): ").strip()

    # ถ้าอาการไม่กรอกให้กำหนดเป็น 'จอปกติดี'
    if not symptom:
        symptom = "จอปกติดี"

    screen_size = input(f"กรุณาใส่ขนาดจอใหม่ (ปัจจุบัน: {entry['ขนาดจอ']}): ").strip()

    # ถ้าไม่กรอกขนาดจอให้กำหนดเป็น 'ไม่ระบุ'
    if not screen_size:
        screen_size = "ไม่ระบุ"

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # อัปเดตข้อมูล
    entry["รายการ"] = item if item else entry["รายการ"]
    entry["s/n"] = serial_number if serial_number else entry["s/n"]
    entry["อาการ"] = symptom
    entry["ขนาดจอ"] = screen_size
    entry["วันที่และเวลาที่ตรวจ"] = timestamp

    # บันทึกข้อมูลลงไฟล์ JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"ข้อมูลของลำดับ {edit_index} ได้รับการอัปเดตเรียบร้อยแล้ว!")








# ฟังก์ชันลบข้อมูล
def delete_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # ถ้าไม่มีข้อมูลในไฟล์
    if not data:
        print("ไม่มีข้อมูลในระบบสำหรับการลบ!")
        return

    # แสดงข้อมูลที่มีอยู่
    print("\n--- ข้อมูลที่มีอยู่ ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ", "ขนาดจอ"
    ))
    print("-" * 105)
    for entry in data:
        # ถ้าไม่มีข้อมูลขนาดจอให้แสดงว่า "ไม่ระบุ"
        screen_size = entry.get("ขนาดจอ", "ไม่ระบุ")
        print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
            entry["ลำดับ"],
            entry["รายการ"],
            entry["s/n"],
            entry["อาการ"],
            entry["วันที่และเวลาที่ตรวจ"],
            screen_size
        ))

    # เลือกข้อมูลที่ต้องการลบ
    while True:
        try:
            delete_index = int(input("\nกรุณาเลือกหมายเลขลำดับที่ต้องการลบ: "))
            # ตรวจสอบว่าหมายเลขลำดับที่เลือกมีอยู่
            entry = next((entry for entry in data if entry["ลำดับ"] == delete_index), None)
            if entry:
                break
            else:
                print("หมายเลขลำดับไม่ถูกต้อง กรุณากรอกใหม่!")
        except ValueError:
            print("กรุณากรอกหมายเลขลำดับที่ถูกต้อง!")

    # แสดงข้อมูลก่อนการลบ
    print(f"\n--- ข้อมูลก่อนการลบ ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ", "ขนาดจอ"
    ))
    print("-" * 105)
    screen_size = entry.get("ขนาดจอ", "ไม่ระบุ")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
        entry["ลำดับ"],
        entry["รายการ"],
        entry["s/n"],
        entry["อาการ"],
        entry["วันที่และเวลาที่ตรวจ"],
        screen_size
    ))

    # ยืนยันการลบข้อมูล
    confirmation = input(f"คุณต้องการลบข้อมูลของลำดับ {delete_index} หรือไม่? (y/n): ").lower()
    if confirmation == 'y':
        # ลบข้อมูล
        data = [entry for entry in data if entry["ลำดับ"] != delete_index]

        # บันทึกข้อมูลลงไฟล์ JSON
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"ข้อมูลของลำดับ {delete_index} ถูกลบเรียบร้อยแล้ว!")
    else:
        print("ยกเลิกการลบข้อมูล.")






# ฟังก์ชันค้นหาข้อมูลจากทุกไฟล์
def search_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # ถ้าไม่มีข้อมูลในไฟล์
    if not data:
        print("ไม่มีข้อมูลในระบบสำหรับการค้นหา!")
        return

    # รับคำค้นหาจากผู้ใช้
    search_term = input("กรุณากรอกคำที่ต้องการค้นหา: ").strip()

    # ค้นหาข้อมูลที่ตรงกับคำค้นหาในทุกๆ ฟิลด์
    found = False
    print("\n--- ผลลัพธ์การค้นหา ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ", "ไฟล์"
    ))
    print("-" * 110)

    # แสดงชื่อไฟล์ในผลลัพธ์
    file_name = os.path.basename(file_path)

    for entry in data:
        # ถ้าคำค้นหาตรงกับข้อมูลในฟิลด์ใดฟิลด์หนึ่ง
        if any(search_term.lower() in str(value).lower() for value in entry.values()):
            found = True
            print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
                entry["ลำดับ"],
                entry["รายการ"],
                entry["s/n"],
                entry["อาการ"],
                entry["วันที่และเวลาที่ตรวจ"],
                file_name  # แสดงชื่อไฟล์
            ))

    if not found:
        print("ไม่พบข้อมูลที่ตรงกับคำค้นหาของคุณ.")







def explain_program():
    explanation = """
    โปรแกรมนี้ออกแบบมาเพื่อจัดการข้อมูลในรูปแบบไฟล์ JSON ภายในโฟลเดอร์ 'check' ที่จะเก็บข้อมูล
    โดยมีฟังก์ชันหลักๆ ที่ให้ผู้ใช้สามารถจัดการกับข้อมูลได้ตามต้องการ

    การทำงานของโปรแกรมจะมีฟังก์ชันหลักๆ ดังนี้:

    1. **initialize_file(filename)**:
       ฟังก์ชันนี้จะทำการตรวจสอบว่าโฟลเดอร์ 'check' และไฟล์ที่ผู้ใช้ระบุ (filename) มีอยู่แล้วหรือไม่
       - ถ้าไฟล์หรือโฟลเดอร์ยังไม่มีอยู่ ฟังก์ชันนี้จะทำการสร้างโฟลเดอร์ 'check' และไฟล์ JSON ใหม่
       - ฟังก์ชันนี้ทำให้ผู้ใช้ไม่ต้องสร้างโฟลเดอร์หรือไฟล์ด้วยตนเอง ทำให้กระบวนการเริ่มต้นของโปรแกรมง่ายขึ้น

    2. **select_file()**:
       ฟังก์ชันนี้ช่วยให้ผู้ใช้สามารถเลือกไฟล์จากไฟล์ที่มีอยู่ในโฟลเดอร์ 'check' 
       - ถ้าไม่มีไฟล์ในโฟลเดอร์ ผู้ใช้สามารถกรอกชื่อไฟล์ใหม่เพื่อสร้างไฟล์ JSON ขึ้นมา
       - ฟังก์ชันนี้ช่วยให้การเลือกไฟล์เพื่อบันทึกข้อมูลสะดวกและมีความยืดหยุ่น

    3. **list_files_in_folder()**:
       ฟังก์ชันนี้จะทำการแสดงรายการไฟล์ทั้งหมดที่มีอยู่ในโฟลเดอร์ 'check'
       - ผู้ใช้สามารถตรวจสอบว่ามีไฟล์อะไรบ้างที่บันทึกข้อมูลอยู่ในโฟลเดอร์นี้
       - ฟังก์ชันนี้ช่วยให้การตรวจสอบไฟล์ที่มีอยู่ในระบบง่ายขึ้น และช่วยลดความสับสนในการทำงานกับไฟล์ต่างๆ

    4. **display_data(file_path)**:
       ฟังก์ชันนี้จะทำการแสดงข้อมูลทั้งหมดที่บันทึกในไฟล์ JSON ที่ระบุ (ผ่านพารามิเตอร์ `file_path`)
       - ข้อมูลจะถูกแสดงในรูปแบบที่อ่านง่าย โดยแสดงลำดับของข้อมูล, หมายเลข S/N, อาการที่เกิดขึ้น, ขนาดจอ, และวันที่/เวลาที่ทำการตรวจสอบ
       - ฟังก์ชันนี้ช่วยให้ผู้ใช้สามารถดูข้อมูลที่เก็บอยู่ในไฟล์ได้อย่างรวดเร็วและสะดวก

    5. **add_data(file_path)**:
       ฟังก์ชันนี้จะช่วยให้ผู้ใช้สามารถเพิ่มข้อมูลใหม่ลงในไฟล์ JSON ได้
       - ผู้ใช้จะต้องกรอกข้อมูลที่เกี่ยวข้อง เช่น 'รายการ', 'S/N', 'อาการ', และ 'ขนาดจอ'
       - ระบบจะทำการเพิ่มข้อมูลใหม่ในไฟล์ JSON โดยอัตโนมัติและปรับลำดับข้อมูลในไฟล์ให้เหมาะสม
       - ฟังก์ชันนี้ช่วยให้การเพิ่มข้อมูลใหม่ในไฟล์สะดวกและรวดเร็ว

    6. **edit_data(file_path)**:
       ฟังก์ชันนี้จะช่วยให้ผู้ใช้สามารถแก้ไขข้อมูลที่มีอยู่ในไฟล์ JSON ได้
       - โปรแกรมจะทำการแสดงรายการข้อมูลทั้งหมดในไฟล์ และให้ผู้ใช้เลือกหมายเลขลำดับที่ต้องการแก้ไข
       - ผู้ใช้สามารถแก้ไขข้อมูลในฟิลด์ต่างๆ เช่น 'รายการ', 'S/N', 'อาการ', และ 'ขนาดจอ'
       - ฟังก์ชันนี้ช่วยให้ผู้ใช้สามารถแก้ไขข้อมูลได้อย่างง่ายดาย

    วิธีการทำงานหลักของโปรแกรม:
    - โปรแกรมจะใช้โฟลเดอร์ 'check' เพื่อเก็บไฟล์ JSON ที่ใช้ในการบันทึกข้อมูล
    - ข้อมูลที่บันทึกในไฟล์ JSON ประกอบด้วย 'ลำดับ', 'รายการ', 'S/N', 'อาการ', 'ขนาดจอ', และ 'วันที่/เวลาในการตรวจสอบ'
    - โปรแกรมจะทำงานร่วมกับไฟล์ JSON เหล่านี้เพื่อเพิ่ม, แก้ไข, แสดงข้อมูล หรือจัดการข้อมูลในรูปแบบต่างๆ ตามที่ผู้ใช้ต้องการ
    """
    
    print(explanation)