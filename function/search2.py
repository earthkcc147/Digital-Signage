# ฟังก์ชันค้นหาข้อมูลจากไฟล์
def search_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # ถ้าไม่มีข้อมูลในไฟล์
    if not data:
        print("ยังไม่มีข้อมูลในระบบสำหรับการค้นหา!")
        return

    # รับคำค้นหาจากผู้ใช้
    search_term = input("กรุณากรอกคำที่ต้องการค้นหา (สามารถค้นหาจาก ลำดับ, รายการ, S/N หรือ อาการ): ").strip()

    # ฟิลเตอร์ข้อมูลที่ตรงกับคำค้นหา
    filtered_data = [
        entry for entry in data
        if search_term in str(entry["ลำดับ"]) or search_term in entry["รายการ"] or search_term in entry["s/n"] or search_term in entry["อาการ"]
    ]

    # แสดงผลลัพธ์การค้นหา
    if filtered_data:
        print("\nผลลัพธ์การค้นหา:")
        print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
            "ลำดับ", "รายการ", "S/N", "อาการ", "วันที่และเวลาที่ตรวจ"
        ))
        print("-" * 90)
        for entry in filtered_data:
            print("{:<5} {:<20} {:<15} {:<30} {:<20}".format(
                entry["ลำดับ"],
                entry["รายการ"],
                entry["s/n"],
                entry["อาการ"],
                entry["วันที่และเวลาที่ตรวจ"]
            ))
    else:
        print(f"ไม่พบข้อมูลที่ตรงกับคำค้นหาของคุณ: '{search_term}'")