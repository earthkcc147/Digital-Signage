# ฟังก์ชันค้นหาข้อมูลจากทุกไฟล์ในโฟลเดอร์
def search_data(file_path=None):
    # ตรวจสอบว่ามีโฟลเดอร์หรือไม่
    if not os.path.exists(FOLDER_NAME):
        print(f"โฟลเดอร์ {FOLDER_NAME} ยังไม่มีอยู่ในระบบ!")
        return

    # รายชื่อไฟล์ในโฟลเดอร์
    files = os.listdir(FOLDER_NAME)
    if not files:
        print("ยังไม่มีไฟล์ในโฟลเดอร์สำหรับการค้นหา!")
        return

    # รับคำค้นหาจากผู้ใช้
    search_term = input("กรุณากรอกคำที่ต้องการค้นหา (สามารถค้นหาจาก ลำดับ, รายการ, S/N, อาการ หรือ ขนาดจอ): ").strip()

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
                print(f"ไม่สามารถอ่านข้อมูลจากไฟล์ {file_name} ได้ (ข้อมูลไม่ถูกต้อง)")
                continue

        # ฟิลเตอร์ข้อมูลที่ตรงกับคำค้นหา
        filtered_data = [
            {**entry, "file_name": file_name}  # เพิ่มชื่อไฟล์ในผลลัพธ์
            for entry in data
            if search_term in str(entry.get("ลำดับ", ""))
            or search_term in entry.get("รายการ", "")
            or search_term in entry.get("s/n", "")
            or search_term in entry.get("อาการ", "")
            or search_term in entry.get("ขนาดจอ", "ไม่ระบุ")
        ]

        # เพิ่มข้อมูลที่ค้นพบในผลลัพธ์
        results.extend(filtered_data)

    # แสดงผลลัพธ์การค้นหา
    if results:
        print("\nผลลัพธ์การค้นหา:")
        print("{:<20} {:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
            "ชื่อไฟล์", "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ", "ขนาดจอ"
        ))
        print("-" * 120)
        for entry in results:
            print("{:<20} {:<5} {:<20} {:<15} {:<30} {:<20} {:<15}".format(
                entry["file_name"],
                entry.get("ลำดับ", "-"),
                entry.get("รายการ", "-"),
                entry.get("s/n", "-"),
                entry.get("อาการ", "-"),
                entry.get("วันที่และเวลาที่ตรวจ", "-"),
                entry.get("ขนาดจอ", "ไม่ระบุ")
            ))
    else:
        print(f"ไม่พบข้อมูลที่ตรงกับคำค้นหาของคุณ: '{search_term}'")