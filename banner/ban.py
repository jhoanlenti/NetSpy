from colorama import Fore, Style, init
from settings import *
from settings.os_check import sistema
import os

# Inicializar colorama
init(autoreset=True)

def netspy_banner():
    banner = f"""
{Fore.WHITE}{Style.BRIGHT}
███╗   ██╗███████╗████████╗███████╗██████╗ ██╗   ██╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚██╗ ██╔╝
██╔██╗ ██║█████╗     ██║   ███████╗██████╔╝ ╚████╔╝ 
██║╚██╗██║██╔══╝     ██║   ╚════██║██╔═══╝   ╚██╔╝  
██║ ╚████║███████╗   ██║   ███████║██║        ██║   
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝        ╚═╝   
"""
    print(banner)
    print("\nBienvenido al Programa de NetSpy. Tu confianza es nuestra prioridad!!! :D")
    print("\n Tool: Network Ports and IPs manangment")
    print("\n\nAuthor: Sergi Pons, Jordi Gomez, Ethan Provencio, Jhoan Sebastian Lope y Nuria Salas")

def banner_1():
    titulo1 = """
        ███████╗██╗███╗   ██╗██████╗      ██╗██████╗ 
        ██╔════╝██║████╗  ██║██╔══██╗     ██║██╔══██╗
        █████╗  ██║██╔██╗ ██║██║  ██║     ██║██████╔╝
        ██╔══╝  ██║██║╚██╗██║██║  ██║     ██║██╔═══╝ 
        ██║     ██║██║ ╚████║██████╔╝     ██║██║     
        ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝      ╚═╝╚═╝     
    """
    if sistema == "windows":
        os.system('cls')
        return print(titulo1)
    elif sistema == "linux":
        os.system('clear')
        return print(titulo1)
    else:
        return False

def banner_2():
    titulo2 = """
        ██╗██████╗     █████╗ ███╗   ██╗ █████╗ ██╗   ██╗     ██╗███████╗███████╗██████╗ 
        ██║██╔══██╗   ██╔══██╗████╗  ██║██╔══██╗██║    ██╗   ██║ ██╔════╝██╔════╝██╔══██╗
        ██║██████╔╝   ███████║██╔██╗ ██║███████║██║     ██║ ██║  ███████╗█████╗  ██████╔╝
        ██║██╔═══╝    ██╔══██║██║╚██╗██║██╔══██║██║       ██║    ╚════██║██╔══╝  ██╔██═╝ 
        ██║██║        ██║  ██║██║ ╚████║██║  ██║███████╗  ██║    ███████║███████╗██║ ██║   
        ╚═╝╚═╝        ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝  ╚═╝    ╚══════╝╚══════╝╚═╝ ╚═╝    
    """
    if sistema == "windows":
        os.system("cls")
        return print(titulo2)
    elif sistema == "linux":
        os.system("clear")
        return print(titulo2)
    else:
        return False

def banner_3(): 
    titulo3 = """
        ██████╗ ██╗   ██╗██████╗  ██╗     ██╗ ██████╗     ██╗██████╗ 
        ██╔══██╗██║   ██║██╔══██╗ ██║     ██║██╔════╝     ██║██╔══██╗
        ██████╔╝██║   ██║██████╔╝ ██║     ██║██║          ██║██████╔╝
        ██╔═══╝ ██║   ██║██╔══██║ ██║     ██║██║          ██║██╔═══╝ 
        ██║     ╚██████╔╝██████╔╝ ███████╗██║╚██████╗     ██║██║     
        ╚═╝      ╚═════╝ ╚═════╝  ╚══════╝╚═╝ ╚═════╝     ╚═╝╚═╝   
    """
    if sistema == "windows":
        os.system("cls")
        return print(titulo3)
    elif sistema == "linux":
        os.system("clear")
        return print(titulo3)
    else:
        return False

def banner_4():
    titulo4 = f"""
        ██╗    ██╗██╗███████╗██╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗
        ██║    ██║██║██╔════╝██║     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
        ██║ █╗ ██║██║█████╗  ██║     ███████║███████║██║     █████╔╝ 
        ██║███╗██║██║██╔══╝  ██║     ██╔══██║██╔══██║██║     ██╔═██╗ 
        ╚███╔███╔╝██║██║     ██║     ██║  ██║██║  ██║╚██████╗██║  ██╗
            ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """
    if sistema == "windows":
        os.system("cls")
        return print(titulo4)
    elif sistema == "linux":
        os.system("clear")
        return print(titulo4)
    else:
        return False