from colorama import init, Fore, Style, Back
import os
import re

# เริ่มต้น colorama เพื่อให้สามารถใช้สีในข้อความได้
init(autoreset=True)





# เริ่มต้น colorama เพื่อให้สามารถใช้สีในข้อความได้
init(autoreset=True)

# ฟังก์ชันพิมพ์เส้นคั่น โดยใช้สีที่กำหนด และขนาดหน้าจอ
def print_line(color=Fore.MAGENTA):
    # คำนวณขนาดของหน้าจอ (จำนวนตัวอักษรในแถว)
    columns, _ = os.get_terminal_size()
    # พิมพ์เส้นคั่นให้เต็มขนาดหน้าจอ
    print(color + "-" * columns + Style.RESET_ALL)



# ฟังก์ชันพิมพ์ข้อความหัวข้อ (header) โดยใช้สีเหลืองและตัวหนา พร้อมความสว่างที่มากขึ้น
def print_header(text):
    print(Fore.BLUE + Style.BRIGHT + "\033[1m" + "\033[1m" + text + "\033[0m")



def print_number(text):
    print(Fore.CYAN + Style.BRIGHT + "\033[1m" + text + "\033[0m")


# ฟังก์ชันสำหรับรับ input และกำหนดสีให้ข้อความ (โดยมีค่าเริ่มต้นเป็นสีเขียว)
def colored_input(prompt, color=Fore.GREEN):
    # ใช้ colorama เพื่อแสดงข้อความในสีที่กำหนดและรีเซ็ตสีหลังจากรับค่า
    return input(color + prompt + Style.RESET_ALL)


# ฟังก์ชันสำหรับรับ input และกำหนดสีให้ข้อความ โดยมีข้อความในวงเล็บเป็นสีเหลืองและตัวหนา
def colored_input2(prompt, color=Fore.GREEN):
    # หาคำในวงเล็บ
    start = prompt.find("(")
    end = prompt.find(")")
    if start != -1 and end != -1:
        # แยกข้อความในวงเล็บและนอกวงเล็บ
        before = prompt[:start]
        in_brackets = prompt[start+1:end]
        after = prompt[end+1:]
        # เปลี่ยนข้อความในวงเล็บเป็นสีเหลืองและตัวหนา
        prompt = before + Fore.YELLOW + "\033[1m" + f"({in_brackets})" + "\033[0m" + Style.RESET_ALL + after
    
    return input(color + prompt + Style.RESET_ALL).strip().lower()









# ฟังก์ชันพิมพ์ข้อความเมนู (menu) โดยใช้สีน้ำเงินอ่อนและตัวอักษรหนา
def print_menu(text):
    print(Fore.CYAN + Style.BRIGHT + text)

# ฟังก์ชันพิมพ์ข้อความเตือน (alarm) โดยใช้สีเหลืองและตัวอักษรหนา
def print_alarm(text):
    print(Fore.YELLOW + Style.BRIGHT + text)

# ฟังก์ชันพิมพ์ข้อความแสดงข้อผิดพลาด (error) โดยใช้สีแดงและตัวอักษรหนา
def print_error(text):
    print(Fore.RED + Style.BRIGHT + text)

# ฟังก์ชันพิมพ์ข้อความแสดงความสำเร็จ (complete) โดยใช้สีเขียวและตัวอักษรหนา
def print_complete(text):
    print(Fore.GREEN + Style.BRIGHT + text)

# ฟังก์ชันพิมพ์ข้อความอื่นๆ (other) โดยใช้สีเขียว
def print_other(text):
    print(Fore.GREEN + text)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีที่กำหนด
def print_background(text, background_color):
    # ใช้ colorama's Back เพื่อกำหนดสีพื้นหลัง
    print(background_color + text)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีแดง
def print_background_red(text):
    print_background(text, Back.RED)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีเขียว
def print_background_green(text):
    print_background(text, Back.GREEN)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีเหลือง
def print_background_yellow(text):
    print_background(text, Back.YELLOW)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีน้ำเงิน
def print_background_blue(text):
    print_background(text, Back.BLUE)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีม่วง
def print_background_magenta(text):
    print_background(text, Back.MAGENTA)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีฟ้า
def print_background_cyan(text):
    print_background(text, Back.CYAN)

# ฟังก์ชันพิมพ์ข้อความที่มีพื้นหลังสีขาว
def print_background_white(text):
    print_background(text, Back.WHITE)