from banner.ban import *
from settings.options import *

def main():
    netspy_banner()
    continuar = True
    while continuar:
        continuar = mode()

if __name__ == "__main__":
    main()