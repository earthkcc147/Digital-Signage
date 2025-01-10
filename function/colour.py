from colorama import init, Fore, Style, Back

# เริ่มต้น colorama เพื่อให้สามารถใช้สีในข้อความได้
init(autoreset=True)

# ฟังก์ชันกำหนดสีสำหรับข้อความต่างๆ

# ฟังก์ชันพิมพ์ข้อความหัวข้อ (header) โดยใช้สีเหลืองและตัวหนา
def print_header(text):
    print(Fore.YELLOW + Style.BRIGHT + "\033[1m" + text + "\033[0m")

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