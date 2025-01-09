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