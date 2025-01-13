from .os_check import sistema
from .ip_linux import lista_ips_lin
from .ip_win import lista_ips_win

def ip_scan():
    if sistema() == "windows":
        lista_ips_win()
    elif sistema() == "linux":
        print("en proceso")
        lista_ips_lin()
    else:
        return False