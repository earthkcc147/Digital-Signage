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