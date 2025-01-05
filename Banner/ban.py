from colorama import Fore, Style, init

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

# Llamar a la función
netspy_banner()
