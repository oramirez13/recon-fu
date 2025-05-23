import whois
import socket
import requests
import os
import platform
from pyfiglet import Figlet

# ========== Función para limpiar pantalla ==========
def limpiar_pantalla():
    # Detecta sistema operativo y ejecuta el comando correspondiente
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# ========== Colores ANSI para el menú ==========
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

from pyfiglet import Figlet

# ========== Colores ANSI ==========
MAGENTA = '\033[95m'
RESET = '\033[0m'

# ========== Banner de la herramienta ==========
def mostrar_banner():
    banner = f"""{GREEN}

██████╗ ███████╗ ██████╗    ██████╗ ███╗   ██╗    ███████╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝   ██╔═══██╗████╗  ██║    ██╔════╝██║   ██║
██████╔╝█████╗  ██║        ██║   ██║██╔██╗ ██║    █████╗  ██║   ██║
██╔══██╗██╔══╝  ██║        ██║   ██║██║╚██╗██║    ██╔══╝  ██║   ██║
██║  ██║███████╗╚██████╗   ╚██████╔╝██║ ╚████║    ██║     ╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═════╝ ╚═╝  ╚═══╝    ╚═╝      ╚═════╝ 
            {MAGENTA}REC ON FU – orami 2025{RESET}
"""
    print(banner)

# ========== Función WHOIS ==========
def whois_lookup(dominio):
    try:
        resultado = whois.whois(dominio)
        print(f"\n{CYAN}[+] Información WHOIS para {dominio}:{RESET}\n")
        print(resultado)
    except Exception as e:
        print(f"{RED}[!] Error al realizar WHOIS: {e}{RESET}")

# ========== Función DNS ==========
def dns_lookup(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        print(f"\n{CYAN}[+] Dirección IP para {dominio}: {RESET}{ip}")
    except socket.gaierror:
        print(f"{RED}[!] No se pudo resolver el dominio.{RESET}")

# ========== Función detección de banner ==========
def detectar_banner_http(dominio):
    try:
        url = f"http://{dominio}"
        response = requests.get(url, timeout=5, verify=False)
        print(f"\n{CYAN}[+] Encabezados HTTP para {dominio}:{RESET}\n")
        for header, valor in response.headers.items():
            print(f"{YELLOW}{header}:{RESET} {valor}")
    except requests.RequestException as e:
        print(f"{RED}[!] Error al conectar con el dominio: {e}{RESET}")

# ========== Menú principal ==========
def mostrar_menu():
    print(f"{GREEN}[1]{RESET} WHOIS Lookup")
    print(f"{GREEN}[2]{RESET} DNS Lookup")
    print(f"{GREEN}[3]{RESET} Detección de banner HTTP")
    print(f"{GREEN}[4]{RESET} Salir")

# ========== Punto de entrada principal ==========
def main():
    limpiar_pantalla()
    mostrar_banner()
    
    while True:
        mostrar_menu()
        opcion = input(f"\n{MAGENTA}[?]{RESET} Ingresa una opción: ")
        
        if opcion == "1":
            dominio = input(f"{CYAN}[>]{RESET} Ingresa el dominio/IP para WHOIS: ")
            whois_lookup(dominio)
        elif opcion == "2":
            dominio = input(f"{CYAN}[>]{RESET} Ingresa el dominio para DNS Lookup: ")
            dns_lookup(dominio)
        elif opcion == "3":
            dominio = input(f"{CYAN}[>]{RESET} Ingresa el dominio para detectar banner: ")
            detectar_banner_http(dominio)
        elif opcion == "4":
            print(f"{YELLOW}[~] Until we meet again, Hacker...{RESET}")
            break
        else:
            print(f"{RED}[!] Opción inválida. Intenta de nuevo.{RESET}")

        input(f"\n{GREEN}Presiona Enter para continuar...{RESET}")
        limpiar_pantalla()
        mostrar_banner()

# ========== Ejecución ==========
if __name__ == "__main__":
    main()
