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