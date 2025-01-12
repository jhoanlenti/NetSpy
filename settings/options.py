from .api import ip_public
from .config_ping import specificip
from .ip import ip_scan
from .wifi_hack_password import hack_password

def mode():
    print(f"\nEscoge que opción prefieres:\n")
    print(f"1. Buscar IP's de mi red activas")
    print(f"2. Analizar IP si está activa")
    print(f"3. IP pública")
    print(f"4. Simulador Hackeo password del WIFI")
    print(f"5. Exit")
        
    while True:
        
        decision = int(input("--> "))
        match decision:    
            case 1:
                titulo1 = """
                    ███████╗██╗███╗   ██╗██████╗      ██╗██████╗ 
                    ██╔════╝██║████╗  ██║██╔══██╗     ██║██╔══██╗
                    █████╗  ██║██╔██╗ ██║██║  ██║     ██║██████╔╝
                    ██╔══╝  ██║██║╚██╗██║██║  ██║     ██║██╔═══╝ 
                    ██║     ██║██║ ╚████║██████╔╝     ██║██║     
                    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝      ╚═╝╚═╝     
                """
                print(titulo1)
                print("En proceso")
                ip_scan()
                # Aquí podrías llamar a la función `pingtodos()`, por ejemplo, para buscar IPs activas en la red.
                return True
            case 2:
                titulo2 = """
                    ██╗██████╗     █████╗ ███╗   ██╗ █████╗ ██╗   ██╗     ██╗███████╗███████╗██████╗ 
                    ██║██╔══██╗   ██╔══██╗████╗  ██║██╔══██╗██║    ██╗   ██║ ██╔════╝██╔════╝██╔══██╗
                    ██║██████╔╝   ███████║██╔██╗ ██║███████║██║     ██║ ██║  ███████╗█████╗  ██████╔╝
                    ██║██╔═══╝    ██╔══██║██║╚██╗██║██╔══██║██║       ██║    ╚════██║██╔══╝  ██╔██═╝ 
                    ██║██║        ██║  ██║██║ ╚████║██║  ██║███████╗  ██║    ███████║███████╗██║ ██║   
                    ╚═╝╚═╝        ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝  ╚═╝    ╚══════╝╚══════╝╚═╝ ╚═╝    
                """
                print(titulo2)
                specificip()  # Esta opción pide una IP y comprueba si está activa
                return True
            case 3:
                titulo3 = """
                    ██████╗ ██╗   ██╗██████╗  ██╗     ██╗ ██████╗     ██╗██████╗ 
                    ██╔══██╗██║   ██║██╔══██╗ ██║     ██║██╔════╝     ██║██╔══██╗
                    ██████╔╝██║   ██║██████╔╝ ██║     ██║██║          ██║██████╔╝
                    ██╔═══╝ ██║   ██║██╔══██║ ██║     ██║██║          ██║██╔═══╝ 
                    ██║     ╚██████╔╝██████╔╝ ███████╗██║╚██████╗     ██║██║     
                    ╚═╝      ╚═════╝ ╚═════╝  ╚══════╝╚═╝ ╚═════╝     ╚═╝╚═╝   
                """
                print(titulo3)
                ip_public(1)
                return True
            case 4:
                titulo4 = f"""
                    ██╗    ██╗██╗███████╗██╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗
                    ██║    ██║██║██╔════╝██║     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
                    ██║ █╗ ██║██║█████╗  ██║     ███████║███████║██║     █████╔╝ 
                    ██║███╗██║██║██╔══╝  ██║     ██╔══██║██╔══██║██║     ██╔═██╗ 
                    ╚███╔███╔╝██║██║     ██║     ██║  ██║██║  ██║╚██████╗██║  ██╗
                     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                """
                print(titulo4)
                averiguar_contraseña = input("Introduce una contraseña ramdom para iniciar el simulador de Hackeo (maximo 8 caracteres): ")
                hack_password(averiguar_contraseña)
                return True
            case 5:
                return False
            case _:
                print("Opción inválida, por favor elige una opción entre 1, 2, 3, 4 o 5")
        
