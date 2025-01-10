from colorama import Fore, Style

# เริ่มต้น colorama
init(autoreset=True)

# ฟังก์ชันกำหนดสีสำหรับข้อความต่างๆ
def print_header(text):
    print(Fore.YELLOW + Style.BRIGHT + "\033[1m" + text + "\033[0m")

def print_menu(text):
    print(Fore.CYAN + Style.BRIGHT + text)

def print_alarm(text):
    print(Fore.YELLOW + Style.BRIGHT + text)

def print_error(text):
    print(Fore.RED + Style.BRIGHT + text)

def print_other(text):
    print(Fore.GREEN + text)