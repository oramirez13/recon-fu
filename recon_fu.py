import whois  # Para obtener información de registro de dominios.
import socket  # Para operaciones de red a bajo nivel (DNS lookup).
import requests  # Para realizar peticiones HTTP y analizar cabeceras.
import os  # Para interactuar con el sistema operativo.
import platform  # Para detectar si el script corre en Arch Linux o Windows.
import subprocess  # Para ejecutar comandos externos como ping.
from pyfiglet import Figlet  # Para generar banners ASCII dinámicos.


# ========== Función para limpiar pantalla ==========
def limpiar_pantalla():
    """Limpia la terminal según el Sistema Operativo detectado."""
    os.system("cls" if platform.system() == "Windows" else "clear")


# ========== Colores ANSI para el menú ==========
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


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
    """Consulta la base de datos WHOIS para obtener datos del propietario."""
    try:
        resultado = whois.whois(dominio)
        print(f"\n{CYAN}[+] Información WHOIS para {dominio}:{RESET}\n")
        print(resultado)
    except Exception as e:
        print(f"{RED}[!] Error al realizar WHOIS: {e}{RESET}")


# ========== Función DNS ==========
def dns_lookup(dominio):
    """Resuelve el nombre de dominio a una dirección IP."""
    try:
        ip = socket.gethostbyname(dominio)
        print(f"\n{CYAN}[+] Dirección IP para {dominio}: {RESET}{ip}")
        return ip
    except socket.gaierror:
        print(f"{RED}[!] No se pudo resolver el dominio.{RESET}")
        return None


# ========== Función detección de banner ==========
def detectar_banner_http(dominio):
    """Analiza las cabeceras HTTP para identificar tecnologías del servidor."""
    try:
        # Añadimos http:// si no lo tiene para que requests no falle.
        url = f"http://{dominio}" if not dominio.startswith("http") else dominio
        # verify=False ignora errores de certificados SSL auto-firmados.
        response = requests.get(url, timeout=5, verify=False)
        print(f"\n{CYAN}[+] Encabezados HTTP para {dominio}:{RESET}\n")
        for header, valor in response.headers.items():
            print(f"{YELLOW}{header}:{RESET} {valor}")
    except requests.RequestException as e:
        print(f"{RED}[!] Error al conectar: {e}{RESET}")


# ========== Función de ping y detección de OS ==========
def ping_y_os(target):
    """Implementación de detección de OS basada en TTL."""
    print(f"\n{CYAN}[+] Haciendo ping a {target} para detección de OS...{RESET}\n")
    param = "-n" if platform.system() == "Windows" else "-c"
    try:
        # Ejecutamos el ping y analizamos el TTL.
        res = subprocess.run(
            ["ping", param, "4", target], capture_output=True, text=True
        )
        salida = res.stdout.lower()
        print(res.stdout)

        if "ttl=128" in salida:
            print(f"{CYAN}[*] OS Detectado: Windows (TTL=128){RESET}")
        elif "ttl=64" in salida:
            print(f"{CYAN}[*] OS Detectado: Linux/Unix (TTL=64){RESET}")
    except Exception as e:
        print(f"{RED}[!] Error en el ping: {e}{RESET}")


# ========== Menú principal ==========
def mostrar_menu():
    print(f"{GREEN}[1]{RESET} WHOIS Lookup")
    print(f"{GREEN}[2]{RESET} DNS Lookup & Detección de OS")
    print(f"{GREEN}[3]{RESET} Detección de banner HTTP")
    print(f"{GREEN}[4]{RESET} Salir")


# ========== Punto de entrada principal ==========
def main():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print(f"{GREEN}[1]{RESET} WHOIS Lookup")
        print(f"{GREEN}[2]{RESET} DNS Lookup & Detección de OS")
        print(f"{GREEN}[3]{RESET} Detección de banner HTTP")
        print(f"{GREEN}[4]{RESET} Salir")

        opcion = input(f"\n{MAGENTA}[?]{RESET} Selecciona una opción: ")

        if opcion == "1":
            dom = input(f"{CYAN}[>]{RESET} Dominio para WHOIS: ")
            whois_lookup(dom)
        elif opcion == "2":
            dom = input(f"{CYAN}[>]{RESET} Dominio para DNS/OS: ")
            ip = dns_lookup(dom)
            if ip:
                ping_y_os(ip)
        elif opcion == "3":
            dom = input(f"{CYAN}[>]{RESET} Dominio para Banner HTTP: ")
            detectar_banner_http(dom)
        elif opcion == "4":
            print(f"{YELLOW}[~] Until we meet again, Hacker...{RESET}")
            break

        input(f"\n{GREEN}Presiona Enter para continuar...{RESET}")


# ========== Ejecución ==========
if __name__ == "__main__":
    main()
# Until we meet again, Hacker...
