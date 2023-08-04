import socket
import subprocess
from termcolor import colored
from _datetime import datetime

target = input("IP Manzilni kiriting: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)
        
        print(f"Maqsadni skanerlash {ip}")
        print("Vaqt boshlandi:", datetime.now())

        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(colored("Ochiq {}: Port".format(port), "red"))
            sock.close()

    except socket.gaierror:
        print("Xost nomini hal qilib bolmadi")
    
    except socket.error:
        print("serverga ulana olmadi")

port_scan(target)