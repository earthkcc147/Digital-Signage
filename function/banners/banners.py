import os
import time
import pyfiglet
import shutil
from colorama import init, Fore, Style

# เริ่มต้นการใช้งาน colorama
init()



# ฟังก์ชันสำหรับจัดข้อความให้อยู่ตรงกลาง
def center_text(text):
    # ดึงขนาดหน้าจอ
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    # แยกข้อความเป็นบรรทัดๆ
    lines = text.splitlines()

    centered_text = ""
    for line in lines:
        # คำนวณพื้นที่ว่างด้านซ้ายเพื่อให้อยู่ตรงกลาง
        centered_line = line.center(terminal_width)
        centered_text += centered_line + "\n"

    return centered_text




# สร้างข้อความ ASCII art ด้วย pyfiglet
intro = pyfiglet.figlet_format("Check\n Display Signage\n", font="calvin_s", width=80)

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def check_display_signage():
    # ใช้ center_text เพื่อจัดข้อความให้อยู่ตรงกลาง
    centered_intro = center_text(intro)
    for line in centered_intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน