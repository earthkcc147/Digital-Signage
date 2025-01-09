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