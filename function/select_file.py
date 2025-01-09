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