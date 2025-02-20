RESET = "\033[0m"
NEGRO = "\033[30m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
BLANCO = "\033[37m"
def color_rgb(texto,rojo,verde,azul):
    return f"\033[38;2;{rojo};{verde};{azul}m{texto}\033[0m"
try:
    nivel_rojo = int(input("Ingrese un numero entre 0 a 255 (nivel rojo): "))
    if nivel_rojo > 255:
        nivel_rojo %= 256
    nivel_verde = int(input("Ingrese un numero entre 0 a 255 (nivel verde): "))
    if nivel_verde > 255:
        nivel_verde %= 256
    nivel_azul = int(input("Ingrese un numero entre 0 a 255 (nivel azul): "))
    if nivel_azul > 255:
        nivel_azul %= 256
    texto = input("Ingrese su texto: ")
    print(color_rgb(texto,nivel_rojo,nivel_verde,nivel_azul))
except Exception as e:
    print(f"{ROJO} Error: {e} ") 

def color_texto_rgb(texto, r, g, b):
    return f"\033[38;2;{r};{g};{b}m{texto}\033[0m"

def color_fondo_rgb(texto, r_texto, g_texto, b_texto, r_fondo, g_fondo, b_fondo):
    return f"\033[48;2;{r_fondo};{g_fondo};{b_fondo}m\033[38;2;{r_texto};{g_texto};{b_texto}m{texto}\033[0m"

# Ejemplo 4.1: Usar la función para texto en un tono de turquesa (RGB: 64, 224, 208)
print(color_texto_rgb("Este texto está en turquesa.", 64, 224, 208))

# Ejemplo 4.2: Usar la función para texto blanco sobre fondo púrpura (RGB: 128, 0, 128)
print(color_fondo_rgb("Texto blanco sobre fondo púrpura.", 255, 255, 255, 128, 0, 128))
# Imprimir texto con diferentes colores
print(f"{ROJO}Este texto es rojo.{RESET}")
print(f"{VERDE}Este texto es verde.{RESET}")
print(f"{AMARILLO}Este texto es amarillo.{RESET}")
print(f"{AZUL}Este texto es azul.{RESET}")
print(f"{MAGENTA}Este texto es magenta.{RESET}")
print(f"{CIAN}Este texto es cian.{RESET}")
print(f"{BLANCO}Este texto es blanco.{RESET}")