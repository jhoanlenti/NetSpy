from .api import ip_public
from .config_ping import specificip
from .ip import ip_scan
from .wifi_hack_password import hack_password

def mode():
    print(f"Escoge que opción prefieres:\n")
    print(f"1. Buscar IP's de mi red activas")
    print(f"2. Analizar IP si está activa")
    print(f"3. IP pública")
    print(f"4. Simulador Hackeo password del WIFI")
        
    while True:
        try:
            decision = int(input("--> "))
            
            if decision == 1:
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
                quit()
            elif decision == 2:
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
                quit()
            elif decision == 3:
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
                quit()
            elif decision == 4:
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
                quit()
            else:
                print("Opción inválida, por favor elige una opción entre 1, 2, 3 o 4.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número entre 1, 2, 3 o 4.")
