from PIL import Image
def textobievenida():
    welcbien = open("bienvenido.txt","r")
    
    print(welcbien.read())

def banner():
    img_path = 'c:\\Users\\06rem\\Downloads\\NetSpy Code\\NetSpy.jpg'

   
    img = Image.open(img_path)

   
    img = img.resize((100, 50))  #ajustar la calidad


    img = img.convert('L')

    # Caracteres ASCII en función del nivel de intensidad
    ascii_chars = "@%#*+=-:. "
    pixels = img.getdata()

    # Asegurar que los valores de píxeles estén dentro del rango adecuado
    ascii_str = "".join([ascii_chars[min(pixel // (256 // len(ascii_chars)), len(ascii_chars) - 1)] for pixel in pixels])

    # Dividir el string en líneas
    width, height = img.size
    ascii_lines = [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]

    for line in ascii_lines:
        print(line)

    textobievenida()

banner()
