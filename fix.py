import subprocess
import sys

# กำหนดโมดูลทั้งหมดที่ต้องการติดตั้งในตัวแปร modules
modules = [
    'beautifulsoup4', 'pyinstaller', 'colorama',  # โมดูล Python
    'openpyxl', 'termcolor', 'colorama',           # ไลบรารี Python เพิ่มเติม
    'build-essential', 'libxml2-dev', 'libxslt-dev', 'zlib-dev', 'clang', 'libffi-dev',  # แพ็คเกจพื้นฐานของ Termux
    'python', 'python-pip'  # Python และ pip
]

# ฟังก์ชันติดตั้งโมดูล Python
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} ติดตั้งสำเร็จ.")
    except subprocess.CalledProcessError as e:
        print(f"ไม่สามารถติดตั้ง {package} ได้: {e}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดขณะติดตั้ง {package}: {e}")

# ฟังก์ชันติดตั้งแพ็คเกจบน Termux
def install_termux_package(package):
    try:
        subprocess.check_call(['pkg', 'install', '-y', package])
        print(f"{package} ติดตั้งสำเร็จใน Termux.")
    except subprocess.CalledProcessError as e:
        print(f"ไม่สามารถติดตั้ง {package} ใน Termux ได้: {e}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดขณะติดตั้ง {package} ใน Termux: {e}")

# ฟังก์ชันอัพเดต Termux และติดตั้ง Python และ pip
def setup_termux():
    try:
        subprocess.check_call(['pkg', 'update', '&&', 'pkg', 'upgrade'], shell=True)
        subprocess.check_call(['pkg', 'install', '-y', 'python', 'python-pip'])
        print("อัพเดต Termux และติดตั้ง Python และ pip สำเร็จ.")
    except subprocess.CalledProcessError as e:
        print(f"ไม่สามารถอัพเดต Termux หรือติดตั้ง Python ได้: {e}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดขณะอัพเดต Termux หรือการติดตั้ง Python: {e}")

# ติดตั้งโมดูล Python และแพ็คเกจ Termux
def install_modules():
    for module in modules:
        try:
            if module in ['python', 'python-pip', 'build-essential', 'libxml2-dev', 'libxslt-dev', 'zlib-dev', 'clang', 'libffi-dev']: 
                print(f"กำลังติดตั้ง {module} ใน Termux...")
                install_termux_package(module)  # ติดตั้งแพ็คเกจใน Termux
            else:
                try:
                    __import__(module)  # ลอง import โมดูล
                    print(f"{module} โมดูลถูกติดตั้งแล้ว.")
                except ImportError as e:
                    print(f"กำลังติดตั้ง {module}...")
                    install_package(module)  # ติดตั้งโมดูล Python
                except Exception as e:
                    print(f"เกิดข้อผิดพลาดขณะติดตั้ง {module}: {e}")
        except Exception as e:
            print(f"ไม่สามารถติดตั้ง {module} ได้: {e}")

# เริ่มต้นการติดตั้ง
try:
    setup_termux()  # อัพเดต Termux และติดตั้ง Python, pip
    install_modules()  # ติดตั้งโมดูลทั้งหมด
    print("การติดตั้งเสร็จสมบูรณ์.")
except Exception as e:
    print(f"เกิดข้อผิดพลาดขณะเริ่มการติดตั้ง: {e}")