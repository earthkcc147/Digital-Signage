import os
import json
import datetime

from function.colour import *


FOLDER_NAME = 'check'


# ฟังก์ชันตรวจสอบและสร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
def initialize_file(filename):
    # ตรวจสอบและสร้างโฟลเดอร์ถ้ายังไม่มี
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print_header(f"\n 🎉 สร้างโฟลเดอร์ {FOLDER_NAME} เรียบร้อยแล้ว 🎉")

    # สร้างไฟล์ในโฟลเดอร์ถ้ายังไม่มี
    file_path = os.path.join(FOLDER_NAME, filename)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)  # สร้างไฟล์พร้อมข้อมูลว่าง
        print_complete(f"\n✅ สร้างไฟล์ {file_path} เรียบร้อยแล้ว ✅")
    else:
        print_error(f"❌ ไฟล์ {file_path} มีอยู่แล้ว ไม่ต้องสร้างใหม่ ❌")
        print_line()

    return file_path








# ฟังก์ชันแสดงรายชื่อไฟล์ในโฟลเดอร์ check
def list_files_in_folder():
    # ตรวจสอบและสร้างโฟลเดอร์ 'check' ถ้ายังไม่มี
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print_header(f"🎉 สร้างโฟลเดอร์ {FOLDER_NAME} เรียบร้อยแล้ว 🎉\n")

    print_header("📂 --- ไฟล์ที่มีอยู่ในโฟลเดอร์ 'check' --- 📂\n")
    files = os.listdir(FOLDER_NAME)
    if files:
        for idx, file in enumerate(files, 1):
            print_number(f"{idx}. {file}\n")
    else:
        print_error("❌ ยังไม่มีไฟล์ในโฟลเดอร์ ❌\n")
        print_line()









# ฟังก์ชันให้ผู้ใช้เลือกไฟล์
def select_file():
    try:
        list_files_in_folder()

        while True:
            file_choice = colored_input("📂 กรุณาเลือกหมายเลขไฟล์ หรือกรอกชื่อไฟล์ใหม่: ").strip()

            # ตรวจสอบว่าเป็นหมายเลข
            if file_choice.isdigit():
                file_choice = int(file_choice)
                files = os.listdir(FOLDER_NAME)
                if 1 <= file_choice <= len(files):
                    return files[file_choice - 1]
                else:
                    print_alarm("⚠️ กรุณาเลือกหมายเลขไฟล์ที่ถูกต้อง! ⚠️")
            else:
                # ตรวจสอบชื่อไฟล์ไม่ให้ว่างเปล่า
                if not file_choice:
                    print_alarm("⚠️ ชื่อไฟล์ไม่สามารถว่างเปล่าได้ กรุณากรอกชื่อไฟล์ใหม่! ⚠️")
                    continue

                # ตรวจสอบว่าไฟล์มีนามสกุล
                if '.' not in file_choice:
                    print_error("❌ ชื่อไฟล์ต้องมีนามสกุล เช่น .txt, .json เป็นต้น กรุณากรอกใหม่! ❌")
                    continue

                filename = file_choice
                file_path = os.path.join(FOLDER_NAME, filename)

                # ตรวจสอบว่าไฟล์มีอยู่แล้วหรือไม่
                if os.path.exists(file_path):
                    print_complete(f"✅ ไฟล์ {filename} มีอยู่แล้ว ไม่ต้องสร้างใหม่. ✅")
                    return filename
                else:
                    print_complete(f"⏳ ไฟล์ {filename} ไม่มีในโฟลเดอร์ 'check' กำลังสร้างไฟล์ใหม่... ⏳")
                    return filename

    except FileNotFoundError:
        print_error(f"❌ ไม่พบโฟลเดอร์ '{FOLDER_NAME}' กรุณาตรวจสอบโฟลเดอร์อีกครั้ง! ❌")
    except PermissionError:
        print_error("❌ ไม่สามารถเข้าถึงโฟลเดอร์หรือไฟล์ได้ กรุณาตรวจสอบสิทธิ์การเข้าถึง! ❌")
    except Exception as e:
        print_error(f"❌ เกิดข้อผิดพลาด: {e} ❌")










# ฟังก์ชันแสดงข้อมูลทั้งหมด
def display_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if data:
                print_line()
                print_number("\n{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
                    "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
                ))
                print_line()
                for entry in data:
                    print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
                        entry["ลำดับ"],
                        entry["รายการ"],
                        entry["s/n"],
                        entry["อาการ"],
                        entry["ขนาดจอ"],
                        entry["วันที่และเวลาที่ตรวจ"]
                    ))
                print_line()
            else:
                print_alarm("⚠️ ไม่มีข้อมูลในระบบ ⚠️\n")
                print_line()
    else:
        print_error("❌ ไม่พบไฟล์ข้อมูลหรือไฟล์เสียหาย ❌\n")
        print_line()








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
        item = colored_input("กรุณาใส่รายการ: ").strip()
        if not item:
            print_alarm("⚠️ กรุณาใส่รายการ ไม่สามารถปล่อยว่างได้! ⚠️")
        else:
            break

    while True:
        serial_number = colored_input("กรุณาใส่ s/n: ").strip()
        if not serial_number:
            print_alarm("⚠️ กรุณาใส่ s/n ไม่สามารถปล่อยว่างได้! ⚠️")
        else:
            break

    # รับข้อมูลอาการ (ให้เลือกจาก y, n หรือกรอกเอง)
    while True:
        symptom_choice = colored_input2("กรุณาเลือกอาการจอ (y = จอปกติ, n = ไม่ระบุ, หรือกรอกเอง): ").strip().lower()
        
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
            print_alarm("⚠️ กรุณาเลือกอาการที่ถูกต้อง! ⚠️")

    # รับข้อมูลขนาดจอ (เลือก n สำหรับ 'ไม่ระบุ')
    while True:
        screen_size = colored_input2("กรุณาใส่ขนาดจอ (ถ้าไม่ระบุให้ใส่ n): ").strip().lower()
        
        if screen_size == 'n':
            screen_size = "ไม่ระบุ"
            break
        elif screen_size:
            break  # ถ้ามีการกรอกขนาดจอเอง
        else:
            print_alarm("⚠️ กรุณาใส่ขนาดจอหรือเลือก 'n' สำหรับไม่ระบุ! ⚠️")

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

    print_complete("✅ บันทึกข้อมูลสำเร็จ! ✅")
    print_line()









# ฟังก์ชันแก้ไขข้อมูล
def edit_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # ถ้าไม่มีข้อมูลในไฟล์
    if not data:
        print_error("❌ ไม่มีข้อมูลในระบบสำหรับการแก้ไข! ❌")
        return

    # แสดงข้อมูลที่มีอยู่
    print_header("\n🎊 --- ข้อมูลที่มีอยู่ --- 🎊")
    print_line()
    print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
    ))
    print_line()
    for entry in data:
        print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
            entry["ลำดับ"],
            entry["รายการ"],
            entry["s/n"],
            entry["อาการ"],
            entry["ขนาดจอ"],
            entry["วันที่และเวลาที่ตรวจ"]
        ))
        print_line()
    # เลือกข้อมูลที่ต้องการแก้ไข
    while True:
        try:
            edit_index = int(colored_input2("\nกรุณาเลือกหมายเลขลำดับที่ต้องการแก้ไข (กรอก 00 เพื่อยกเลิก): "))

            # หากกรอก 00 ให้ยกเลิกการแก้ไข
            if edit_index == 00:
                print_complete("✅ ยกเลิกการแก้ไขข้อมูล ✅")
                return

            # ตรวจสอบว่าหมายเลขลำดับที่เลือกมีอยู่
            entry = next((entry for entry in data if entry["ลำดับ"] == edit_index), None)
            if entry:
                break
            else:
                print_alarm("⚠️ หมายเลขลำดับไม่ถูกต้อง กรุณากรอกใหม่! ⚠️")
                print_line()
        except ValueError:
            print_alarm("⚠️ กรุณากรอกหมายเลขลำดับที่ถูกต้อง! ⚠️")
            print_line()

    # แสดงข้อมูลก่อนการแก้ไข
    print_header(f"\n--- ข้อมูลก่อนการแก้ไข ---")
    print_line()
    print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
    ))
    print_line()
    print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        entry["ลำดับ"],
        entry["รายการ"],
        entry["s/n"],
        entry["อาการ"],
        entry["ขนาดจอ"],
        entry["วันที่และเวลาที่ตรวจ"]
    ))
    print_line()

    # แก้ไขข้อมูล
    item = colored_input2(f"กรุณาใส่รายการใหม่ (ปัจจุบัน: {entry['รายการ']} หรือกรอก 00 เพื่อยกเลิก): ").strip()
    if item == "00":
        print_complete("✅ ยกเลิกการแก้ไขข้อมูล ✅")
        return

    serial_number = colored_input2(f"กรุณาใส่ s/n ใหม่ (ปัจจุบัน: {entry['s/n']} หรือกรอก 00 เพื่อยกเลิก): ").strip()
    if serial_number == "00":
        print_complete("✅ ยกเลิกการแก้ไขข้อมูล ✅")
        return

    symptom = colored_input2(f"กรุณาใส่อาการใหม่ (ปัจจุบัน: {entry['อาการ']} หรือกรอก 00 เพื่อยกเลิก): ").strip()
    if symptom == "00":
        print_complete("✅ ยกเลิกการแก้ไขข้อมูล ✅")
        return

    # ถ้าอาการไม่กรอกให้กำหนดเป็น 'จอปกติดี'
    if not symptom:
        symptom = "จอปกติดี"

    screen_size = colored_input2(f"กรุณาใส่ขนาดจอใหม่ (ปัจจุบัน: {entry['ขนาดจอ']} หรือกรอก 00 เพื่อยกเลิก): ").strip()
    if screen_size == "00":
        print_complete("✅ ยกเลิกการแก้ไขข้อมูล ✅")
        return

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

    print_complete(f"✅ ข้อมูลของลำดับ {edit_index} ได้รับการอัปเดตเรียบร้อยแล้ว! ✅")
    print_line()










# ฟังก์ชันลบข้อมูล
def delete_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # ถ้าไม่มีข้อมูลในไฟล์
    if not data:
        print_alarm("⚠️ ไม่มีข้อมูลในระบบสำหรับการลบ! ⚠️")
        return

    # แสดงข้อมูลที่มีอยู่
    print_header("\n--- ข้อมูลที่มีอยู่ ---")
    print_line()
    print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ", "ขนาดจอ"
    ))
    print_line()
    for entry in data:
        # ถ้าไม่มีข้อมูลขนาดจอให้แสดงว่า "ไม่ระบุ"
        screen_size = entry.get("ขนาดจอ", "ไม่ระบุ")
        print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
            entry["ลำดับ"],
            entry["รายการ"],
            entry["s/n"],
            entry["อาการ"],
            entry["วันที่และเวลาที่ตรวจ"],
            screen_size
        ))
        print_line()
    # เลือกข้อมูลที่ต้องการลบ
    while True:
        try:
            delete_index = int(colored_input("\nกรุณาเลือกหมายเลขลำดับที่ต้องการลบ: "))
            # ตรวจสอบว่าหมายเลขลำดับที่เลือกมีอยู่
            entry = next((entry for entry in data if entry["ลำดับ"] == delete_index), None)
            if entry:
                break
            else:
                print_alarm("⚠️ หมายเลขลำดับไม่ถูกต้อง กรุณากรอกใหม่! ⚠️")
                print_line()
        except ValueError:
            print_alarm("⚠️ กรุณากรอกหมายเลขลำดับที่ถูกต้อง! ⚠️")
            print_line()

    # แสดงข้อมูลก่อนการลบ
    print_header(f"\n--- ข้อมูลก่อนการลบ ---")
    print_line()
    print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ", "ขนาดจอ"
    ))
    print_line()
    screen_size = entry.get("ขนาดจอ", "ไม่ระบุ")
    print_number("{:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
        entry["ลำดับ"],
        entry["รายการ"],
        entry["s/n"],
        entry["อาการ"],
        entry["วันที่และเวลาที่ตรวจ"],
        screen_size
    ))
    print_line()

    # ยืนยันการลบข้อมูล
    confirmation = colored_input2(f"คุณต้องการลบข้อมูลของลำดับ {delete_index} หรือไม่? (y/n): ").lower()
    if confirmation == 'y':
        # ลบข้อมูล
        data = [entry for entry in data if entry["ลำดับ"] != delete_index]

        # บันทึกข้อมูลลงไฟล์ JSON
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print_complete(f"✅ ข้อมูลของลำดับ {delete_index} ถูกลบเรียบร้อยแล้ว! ✅")
        print_line()
    else:
        print_complete("✅ ยกเลิกการลบข้อมูล. ✅")
        print_line()











# ฟังก์ชันค้นหาข้อมูลจากทุกไฟล์ในโฟลเดอร์
def search_data(file_path):
    # ตรวจสอบว่ามีโฟลเดอร์หรือไม่
    if not os.path.exists(FOLDER_NAME):
        print_alarm(f"⚠️ โฟลเดอร์ 📂 {FOLDER_NAME} ยังไม่มีอยู่ในระบบ! ⚠️")
        print_line()
        return

    # รายชื่อไฟล์ในโฟลเดอร์
    files = os.listdir(FOLDER_NAME)
    if not files:
        print_alarm("⚠️ ยังไม่มีไฟล์ในโฟลเดอร์ 📂 สำหรับการค้นหา! ⚠️")
        print_line()
        return

    # รับคำค้นหาจากผู้ใช้
    search_term = colored_input2("กรุณากรอกคำที่ต้องการค้นหา (สามารถค้นหาจาก ลำดับ, รายการ, S/N, อาการ หรือ ขนาดจอ): ").strip()

    # ตัวแปรสำหรับเก็บผลลัพธ์
    results = []

    # ค้นหาในทุกไฟล์
    for file_name in files:
        file_path = os.path.join(FOLDER_NAME, file_name)

        # ข้ามไฟล์ที่ไม่ใช่ JSON
        if not file_name.endswith(".json"):
            continue

        # อ่านข้อมูลจากไฟล์
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print_error(f"❌ ไม่สามารถอ่านข้อมูลจากไฟล์ {file_name} ได้ (ข้อมูลไม่ถูกต้อง) ❌")
                continue

        # ฟิลเตอร์ข้อมูลที่ตรงกับคำค้นหา
        filtered_data = [
            {**entry, "file_name": file_name}  # เพิ่มชื่อไฟล์ในผลลัพธ์
            for entry in data
            if (search_term.lower() in str(entry.get("ลำดับ", "")).lower() or
                search_term.lower() in entry.get("รายการ", "").lower() or
                search_term.lower() in entry.get("s/n", "").lower() or
                search_term.lower() in entry.get("อาการ", "").lower() or
                search_term.lower() in entry.get("ขนาดจอ", "ไม่ระบุ").lower())
        ]

        # เพิ่มข้อมูลที่ค้นพบในผลลัพธ์
        results.extend(filtered_data)

    # แสดงผลลัพธ์การค้นหา
    if results:
        print_header("\nผลลัพธ์การค้นหา:")
        print_line()
        print_number("{:<20} {:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
            "ชื่อไฟล์", "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ", "ขนาดจอ"
        ))
        print_line()
        for entry in results:
            print_number("{:<20} {:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
                entry["file_name"],
                entry.get("ลำดับ", "-"),
                entry.get("รายการ", "-"),
                entry.get("s/n", "-"),
                entry.get("อาการ", "-"),
                entry.get("วันที่และเวลาที่ตรวจ", "-"),
                entry.get("ขนาดจอ", "ไม่ระบุ")
            ))
            print_line()

        # รอให้ผู้ใช้กด Enter เพื่อย้อนกลับ
        colored_input("\nกด Enter เพื่อย้อนกลับ...")  # กด Enter เพื่อย้อนกลับ
        print_complete("🔄 ย้อนกลับแล้ว! 🔄")
        print_line()
        return
    else:
        print_alarm(f"⚠️ ไม่พบข้อมูลที่ตรงกับคำค้นหาของคุณ: '{search_term}' ⚠️")
        print_line()
        # รอให้ผู้ใช้กด Enter เพื่อย้อนกลับ
        colored_input("\nกด Enter เพื่อย้อนกลับ...")  # กด Enter เพื่อย้อนกลับ
        print_complete("🔄 ย้อนกลับแล้ว!🔄 ")
        print_line()
        return



# ฟังก์ชันลบไฟล์พร้อมการยืนยัน
def delete_file():
    try:
        # รับชื่อไฟล์จากผู้ใช้
        file_name = colored_input2("กรุณากรอกชื่อไฟล์ที่ต้องการลบ: ").strip()
        file_path = os.path.join(FOLDER_NAME, file_name)

        # ตรวจสอบว่าไฟล์มีอยู่หรือไม่
        if os.path.exists(file_path):
            # แสดงข้อมูลในไฟล์
            print(f"\nข้อมูลในไฟล์ {file_name}:")
            display_data(file_path)

            # ขอการยืนยันจากผู้ใช้
            confirm = colored_input2("\nคุณต้องการลบไฟล์นี้ใช่หรือไม่? (y/n): ").strip().lower()
            if confirm == 'y':
                # ลบไฟล์
                os.remove(file_path)
                print_complete(f"✅ ลบไฟล์ {file_name} เรียบร้อยแล้ว ✅")
                print_line()
            else:
                print("❌ การลบไฟล์ถูกยกเลิก ❌")
                print_line()
        else:
            print_error(f"❌ ไม่พบไฟล์ {file_name} ในโฟลเดอร์ '{FOLDER_NAME}' ❌")
            print_line()

    except Exception as e:
        print_error(f"❌ เกิดข้อผิดพลาดในการลบไฟล์: {e} ❌")
        print_line()





def explain_program():
    explanation = """
    โปรแกรมนี้ออกแบบมาเพื่อจัดการข้อมูลในรูปแบบไฟล์ JSON ภายในโฟลเดอร์ 'check' ที่จะเก็บข้อมูล
    โดยมีฟังก์ชันหลักๆ ที่ให้ผู้ใช้สามารถจัดการกับข้อมูลได้ตามต้องการ

    การทำงานของโปรแกรมจะมีฟังก์ชันหลักๆ ดังนี้:

    1. 🗂️ **initialize_file(filename)**:
       ฟังก์ชันนี้จะทำการตรวจสอบว่าโฟลเดอร์ 'check' และไฟล์ที่ผู้ใช้ระบุ (filename) มีอยู่แล้วหรือไม่
       - ถ้าไฟล์หรือโฟลเดอร์ยังไม่มีอยู่ ฟังก์ชันนี้จะทำการสร้างโฟลเดอร์ 'check' และไฟล์ JSON ใหม่
       - ฟังก์ชันนี้ทำให้ผู้ใช้ไม่ต้องสร้างโฟลเดอร์หรือไฟล์ด้วยตนเอง ทำให้กระบวนการเริ่มต้นของโปรแกรมง่ายขึ้น

    2. 📝 **select_file()**:
       ฟังก์ชันนี้ช่วยให้ผู้ใช้สามารถเลือกไฟล์จากไฟล์ที่มีอยู่ในโฟลเดอร์ 'check' 
       - ถ้าไม่มีไฟล์ในโฟลเดอร์ ผู้ใช้สามารถกรอกชื่อไฟล์ใหม่เพื่อสร้างไฟล์ JSON ขึ้นมา
       - ฟังก์ชันนี้ช่วยให้การเลือกไฟล์เพื่อบันทึกข้อมูลสะดวกและมีความยืดหยุ่น

    3. 📁 **list_files_in_folder()**:
       ฟังก์ชันนี้จะทำการแสดงรายการไฟล์ทั้งหมดที่มีอยู่ในโฟลเดอร์ 'check'
       - ผู้ใช้สามารถตรวจสอบว่ามีไฟล์อะไรบ้างที่บันทึกข้อมูลอยู่ในโฟลเดอร์นี้
       - ฟังก์ชันนี้ช่วยให้การตรวจสอบไฟล์ที่มีอยู่ในระบบง่ายขึ้น และช่วยลดความสับสนในการทำงานกับไฟล์ต่างๆ

    4. 👁️‍🗨️ **display_data(file_path)**:
       ฟังก์ชันนี้จะทำการแสดงข้อมูลทั้งหมดที่บันทึกในไฟล์ JSON ที่ระบุ (ผ่านพารามิเตอร์ `file_path`)
       - ข้อมูลจะถูกแสดงในรูปแบบที่อ่านง่าย โดยแสดงลำดับของข้อมูล, หมายเลข S/N, อาการที่เกิดขึ้น, ขนาดจอ, และวันที่/เวลาที่ทำการตรวจสอบ
       - ฟังก์ชันนี้ช่วยให้ผู้ใช้สามารถดูข้อมูลที่เก็บอยู่ในไฟล์ได้อย่างรวดเร็วและสะดวก

    5. ➕ **add_data(file_path)**:
       ฟังก์ชันนี้จะช่วยให้ผู้ใช้สามารถเพิ่มข้อมูลใหม่ลงในไฟล์ JSON ได้
       - ผู้ใช้จะต้องกรอกข้อมูลที่เกี่ยวข้อง เช่น 'รายการ', 'S/N', 'อาการ', และ 'ขนาดจอ'
       - ระบบจะทำการเพิ่มข้อมูลใหม่ในไฟล์ JSON โดยอัตโนมัติและปรับลำดับข้อมูลในไฟล์ให้เหมาะสม
       - ฟังก์ชันนี้ช่วยให้การเพิ่มข้อมูลใหม่ในไฟล์สะดวกและรวดเร็ว

    6. ✏️ **edit_data(file_path)**:
       ฟังก์ชันนี้จะช่วยให้ผู้ใช้สามารถแก้ไขข้อมูลที่มีอยู่ในไฟล์ JSON ได้
       - โปรแกรมจะทำการแสดงรายการข้อมูลทั้งหมดในไฟล์ และให้ผู้ใช้เลือกหมายเลขลำดับที่ต้องการแก้ไข
       - ผู้ใช้สามารถแก้ไขข้อมูลในฟิลด์ต่างๆ เช่น 'รายการ', 'S/N', 'อาการ', และ 'ขนาดจอ'
       - ฟังก์ชันนี้ช่วยให้ผู้ใช้สามารถแก้ไขข้อมูลได้อย่างง่ายดาย

    วิธีการทำงานหลักของโปรแกรม:
    - โปรแกรมจะใช้โฟลเดอร์ 'check' เพื่อเก็บไฟล์ JSON ที่ใช้ในการบันทึกข้อมูล
    - ข้อมูลที่บันทึกในไฟล์ JSON ประกอบด้วย 'ลำดับ', 'รายการ', 'S/N', 'อาการ', 'ขนาดจอ', และ 'วันที่/เวลาในการตรวจสอบ'
    - โปรแกรมจะทำงานร่วมกับไฟล์ JSON เหล่านี้เพื่อเพิ่ม, แก้ไข, แสดงข้อมูล หรือจัดการข้อมูลในรูปแบบต่างๆ ตามที่ผู้ใช้ต้องการ
    """

    print_header("คำอธิบายโปรแกรม:")
    print_line()
    print_other(explanation)
    print_line()