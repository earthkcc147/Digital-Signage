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