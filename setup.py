import os
import subprocess
import json
from colorama import init, Fore, Style

# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

# ตัวแปรสำหรับกำหนดชื่อไฟล์ JSON
json_file = 'install_git.json'

# ฟังก์ชันสำหรับติดตั้งข้อมูลจาก GitHub
def install_from_github(repo_url, repo_name, program_name):
    try:
        # แสดงชื่อโปรแกรมที่กำลังติดตั้ง
        print(f"\n{Fore.YELLOW}กำลังติดตั้งโปรแกรม: {program_name}")
        
        # ตรวจสอบว่ามีโฟลเดอร์ที่ต้องการติดตั้งอยู่แล้วหรือไม่
        if os.path.exists(repo_name):
            print(f"{Fore.GREEN}✔ โฟลเดอร์ {repo_name} มีอยู่แล้ว! กำลังอัปเดตข้อมูล...")
            # เปลี่ยนไปยังโฟลเดอร์ที่มีอยู่แล้วและดึงข้อมูลใหม่
            os.chdir(repo_name)
            subprocess.run(["git", "pull"], check=True)
            print(f"{Fore.CYAN}🔄 การอัปเดตข้อมูลจาก {repo_url} เสร็จสมบูรณ์")
        else:
            print(f"{Fore.YELLOW}⏳ กำลังติดตั้งข้อมูลจาก {repo_url}...")
            # ดึงข้อมูลจาก GitHub
            subprocess.run(["git", "clone", repo_url, repo_name], check=True)
            print(f"{Fore.GREEN}✅ การติดตั้ง {program_name} เสร็จสมบูรณ์!")

        print(f"\n{Fore.GREEN}✔ การติดตั้ง {program_name} เสร็จสมบูรณ์!\n")
    
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}❌ เกิดข้อผิดพลาดในการติดตั้ง {program_name} จาก {repo_url}: {e}")
    except Exception as e:
        print(f"{Fore.RED}⚠️ เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")

# ฟังก์ชันอ่านไฟล์ JSON และติดตั้งโปรแกรม
def install_programs_from_json(json_file):
    try:
        # ตรวจสอบว่าไฟล์ JSON มีอยู่หรือไม่
        if not os.path.exists(json_file):
            print(f"{Fore.RED}❌ ไม่พบไฟล์ {json_file}! กำลังสร้างไฟล์เริ่มต้น...")
            create_default_json(json_file)

        # เปิดไฟล์ JSON และโหลดข้อมูล
        with open(json_file, 'r', encoding='utf-8') as file:
            programs = json.load(file)

        # วนลูปติดตั้งโปรแกรมจากข้อมูลใน JSON
        for program in programs:
            program_name = program.get("program_name")
            repo_url = program.get("repo_url")
            if program_name and repo_url:
                repo_name = repo_url.split("/")[-1].replace(".git", "")
                install_from_github(repo_url, repo_name, program_name)
            else:
                print(f"{Fore.RED}❌ ข้อมูลโปรแกรมไม่ครบถ้วนใน JSON: {program}")

    except json.JSONDecodeError:
        print(f"{Fore.RED}❌ ข้อมูลในไฟล์ {json_file} ไม่ถูกต้อง! กรุณาตรวจสอบไฟล์ JSON")
    except FileNotFoundError:
        print(f"{Fore.RED}❌ ไม่พบไฟล์ {json_file}! กรุณาตรวจสอบว่าไฟล์มีอยู่ในที่ตั้งที่ถูกต้อง")
    except Exception as e:
        print(f"{Fore.RED}⚠️ เกิดข้อผิดพลาดในการติดตั้งโปรแกรมจากไฟล์ {json_file}: {e}")

# ฟังก์ชันสร้างไฟล์ JSON เริ่มต้น
def create_default_json(json_file):
    try:
        # ข้อมูลเริ่มต้นสำหรับไฟล์ JSON
        default_data = [
            {
                "program_name": "Digital-Signage",
                "repo_url": "https://github.com/earthkcc147/Digital-Signage.git"
            },
            {
                "program_name": "Another-Program",
                "repo_url": "https://github.com/username/another-program.git"
            }
        ]
        
        # เขียนข้อมูลเริ่มต้นลงในไฟล์ JSON
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(default_data, file, indent=4, ensure_ascii=False)
        
        print(f"{Fore.GREEN}✔ ไฟล์ {json_file} ถูกสร้างขึ้นมาแล้ว!")

    except Exception as e:
        print(f"{Fore.RED}⚠️ เกิดข้อผิดพลาดในการสร้างไฟล์ {json_file}: {e}")

# ฟังก์ชันแสดงคำอธิบายการทำงานของโปรแกรม
def show_program_description():
    description = """
    โปรแกรมนี้ช่วยในการติดตั้งโปรแกรมจาก GitHub โดยทำงานตามขั้นตอนดังนี้:
    
    1. อ่านไฟล์ JSON ที่มีข้อมูลโปรแกรมที่ต้องการติดตั้งจาก GitHub
    2. ตรวจสอบว่าโฟลเดอร์โปรแกรมนั้น ๆ มีอยู่หรือไม่:
        - หากมีอยู่แล้วจะทำการอัปเดตข้อมูลล่าสุดจาก GitHub
        - หากไม่มี จะทำการติดตั้งโปรแกรมใหม่
    3. หากการติดตั้งหรืออัปเดตสำเร็จ จะแสดงข้อความยืนยันการติดตั้งสำเร็จ
    4. หากเกิดข้อผิดพลาด จะแสดงข้อความแจ้งเตือนข้อผิดพลาด
    
    ตัวเลือกเมนู:
    - เลือก 1: ติดตั้งโปรแกรมจากไฟล์ JSON
    - เลือก 2: ออกจากโปรแกรม
    """
    print(f"{Fore.CYAN}{description}")

# ฟังก์ชันเมนูหลัก
def main_menu():
    while True:
        print(f"\n{Fore.CYAN}===== เมนูหลัก =====")
        print(f"{Fore.YELLOW}1. ติดตั้งโปรแกรมจากไฟล์ JSON")
        print(f"{Fore.YELLOW}2. อธิบายการทำงานของโปรแกรม")
        print(f"{Fore.YELLOW}3. ออกจากโปรแกรม")
        
        choice = input(f"\n{Fore.GREEN}กรุณาเลือกตัวเลือก (1/2/3): ")

        if choice == '1':
            install_programs_from_json(json_file)
        elif choice == '2':
            show_program_description()
        elif choice == '3':
            print(f"{Fore.RED}ออกจากโปรแกรม...")
            break
        else:
            print(f"{Fore.RED}❌ ตัวเลือกไม่ถูกต้อง! กรุณาเลือกใหม่.")

# เรียกใช้งานเมนูหลัก
main_menu()