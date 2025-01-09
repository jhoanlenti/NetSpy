from colorama import Fore, Style, init
from settings import *

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
    print("\n\nAuthor: Sergi, Jordi, Ethan, Jhoan y Nuria")