from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def netspy_banner():
    banner = f"""
{Fore.RED}███╗   ██╗███████╗████████╗███████╗███████╗██████╗ ██╗   ██╗
{Fore.RED}████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝
{Fore.RED}██╔██╗ ██║█████╗     ██║   █████╗  █████╗  ██████╔╝ ╚████╔╝ 
{Fore.RED}██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██╔══╝  ██╔═══╝   ╚██╔╝  
{Fore.RED}██║ ╚████║███████╗   ██║   ███████╗██║     ██║        ██║   
{Fore.RED}╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝        ╚═╝   
{Fore.GREEN}                  Network Monitoring Tool                  
{Fore.YELLOW}                  Author: Your Name Here                  
    """
    print(banner)

# Llamar a la función
netspy_banner()
