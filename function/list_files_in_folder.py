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