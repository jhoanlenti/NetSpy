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
    print("\nBienvenido al Programa de NetSpy. Tu confianza es nuestra prioridad!!! :D")

# Llamar a la función
netspy_banner()
