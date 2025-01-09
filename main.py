import os
import json
import datetime

# ชื่อโฟลเดอร์
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

    symptom = input("กรุณาใส่อาการ (ถ้าไม่มีกรอกกด Enter เพื่อใช้ค่า 'จอปกติดี'): ")

    # ถ้าอาการไม่กรอกให้กำหนดเป็น 'จอปกติดี'
    if not symptom.strip():  # ถ้าค่าที่กรอกมาเป็นค่าว่าง
        symptom = "จอปกติดี"  # กำหนดอาการเป็น "จอปกติดี"

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # เพิ่มข้อมูลใหม่
    new_entry = {
        "ลำดับ": sequence,
        "รายการ": item,
        "s/n": serial_number,
        "อาการ": symptom,
        "วันที่และเวลาที่ตรวจ": timestamp
    }
    data.append(new_entry)

    # บันทึกข้อมูลลงไฟล์ JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("บันทึกข้อมูลสำเร็จ!")

# ฟังก์ชันแสดงข้อมูลทั้งหมด
def display_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if data:
                print("\n{:<5} {:<20} {:<15} {:<30} {:<20}".format(
                    "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ"
                ))
                print("-" * 90)
                for entry in data:
                    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
                        entry["ลำดับ"],
                        entry["รายการ"],
                        entry["s/n"],
                        entry["อาการ"],
                        entry["วันที่และเวลาที่ตรวจ"]
                    ))
            else:
                print("ยังไม่มีข้อมูลในระบบ")
    else:
        print("ยังไม่มีข้อมูลในระบบ")

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
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 90)
    for entry in data:
        print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
            entry["ลำดับ"],
            entry["รายการ"],
            entry["s/n"],
            entry["อาการ"],
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
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 90)
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        entry["ลำดับ"],
        entry["รายการ"],
        entry["s/n"],
        entry["อาการ"],
        entry["วันที่และเวลาที่ตรวจ"]
    ))

    # แก้ไขข้อมูล
    item = input(f"กรุณาใส่รายการใหม่ (ปัจจุบัน: {entry['รายการ']}): ").strip()
    if item == "00":  # ถ้ากรอก 00 ให้ยกเลิกการแก้ไข
        print("ยกเลิกการแก้ไขข้อมูล.")
        return

    serial_number = input(f"กรุณาใส่ s/n ใหม่ (ปัจจุบัน: {entry['s/n']}): ").strip()
    if serial_number == "00":  # ถ้ากรอก 00 ให้ยกเลิกการแก้ไข
        print("ยกเลิกการแก้ไขข้อมูล.")
        return

    symptom = input(f"กรุณาใส่อาการใหม่ (ปัจจุบัน: {entry['อาการ']}): ").strip()
    if symptom == "00":  # ถ้ากรอก 00 ให้ยกเลิกการแก้ไข
        print("ยกเลิกการแก้ไขข้อมูล.")
        return

    # ถ้าอาการไม่กรอกให้กำหนดเป็น 'จอปกติดี'
    if not symptom:
        symptom = "จอปกติดี"

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # แสดงข้อมูลหลังการแก้ไข
    print(f"\n--- ข้อมูลหลังการแก้ไข ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 90)
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        edit_index,
        item if item else entry["รายการ"],
        serial_number if serial_number else entry["s/n"],
        symptom,
        timestamp
    ))

    # ยืนยันการบันทึกการแก้ไข
    confirmation = input(f"\nคุณต้องการบันทึกการแก้ไขข้อมูลของลำดับ {edit_index} หรือไม่? (y/n): ").lower()
    if confirmation == 'y':
        # อัปเดตข้อมูล
        entry["รายการ"] = item if item else entry["รายการ"]
        entry["s/n"] = serial_number if serial_number else entry["s/n"]
        entry["อาการ"] = symptom
        entry["วันที่และเวลาที่ตรวจ"] = timestamp

        # บันทึกข้อมูลลงไฟล์ JSON
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"ข้อมูลของลำดับ {edit_index} ได้รับการอัปเดตเรียบร้อยแล้ว!")
    else:
        print("ยกเลิกการบันทึกการแก้ไขข้อมูล.")

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
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 90)
    for entry in data:
        print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
            entry["ลำดับ"],
            entry["รายการ"],
            entry["s/n"],
            entry["อาการ"],
            entry["วันที่และเวลาที่ตรวจ"]
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
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 90)
    print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
        entry["ลำดับ"],
        entry["รายการ"],
        entry["s/n"],
        entry["อาการ"],
        entry["วันที่และเวลาที่ตรวจ"]
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

# ฟังก์ชันหลัก
def main():
    # เลือกไฟล์
    filename = select_file()

    # สร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
    file_path = initialize_file(filename)

    while True:
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

# เรียกใช้งานเมนูหลัก
if __name__ == '__main__':
    main()

