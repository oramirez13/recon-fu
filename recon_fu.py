import os
import platform
import socket
import subprocess

import requests
import whois

# Estas constantes guardan colores ANSI simples para la terminal.
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


def limpiar_pantalla():
    # Esta funcion limpia la terminal segun el sistema operativo.
    os.system("cls" if platform.system() == "Windows" else "clear")


def mostrar_banner():
    # Este bloque imprime el titulo principal del proyecto.
    print(
        f"""{GREEN}
██████╗ ███████╗ ██████╗    ██████╗ ███╗   ██╗    ███████╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝   ██╔═══██╗████╗  ██║    ██╔════╝██║   ██║
██████╔╝█████╗  ██║        ██║   ██║██╔██╗ ██║    █████╗  ██║   ██║
██╔══██╗██╔══╝  ██║        ██║   ██║██║╚██╗██║    ██╔══╝  ██║   ██║
██║  ██║███████╗╚██████╗   ╚██████╔╝██║ ╚████║    ██║     ╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═════╝ ╚═╝  ╚═══╝    ╚═╝      ╚═════╝ 
            {MAGENTA}Recon Fu{RESET}
"""
    )


def pause():
    # Esta funcion espera hasta que el usuario presione Enter.
    input(f"\n{GREEN}Presiona Enter para continuar...{RESET}")


def pedir_dominio(message):
    # Esta funcion pide un dato al usuario y recorta espacios sobrantes.
    return input(message).strip()


def whois_lookup(domain):
    # Si el dominio viene vacio, detenemos la funcion.
    if domain == "":
        print(f"{RED}[!] Debes ingresar un dominio valido.{RESET}")
        return

    try:
        # Esta linea realiza la consulta WHOIS.
        result = whois.whois(domain)
    except Exception as error:
        # Si falla la consulta, se muestra el error real.
        print(f"{RED}[!] Error al realizar WHOIS: {error}{RESET}")
        return

    # Estas lineas imprimen el contenido recibido.
    print(f"\n{CYAN}[+] Informacion WHOIS para {domain}:{RESET}\n")
    print(result)


def dns_lookup(domain):
    # Si el dominio esta vacio, no tiene sentido continuar.
    if domain == "":
        print(f"{RED}[!] Debes ingresar un dominio valido.{RESET}")
        return None

    try:
        # Esta linea resuelve el dominio a una IP.
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        # Si falla la resolucion, devolvemos None.
        print(f"{RED}[!] No se pudo resolver el dominio.{RESET}")
        return None

    # Esta linea muestra la IP encontrada.
    print(f"\n{CYAN}[+] Direccion IP para {domain}:{RESET} {ip}")
    return ip


def detectar_banner_http(domain):
    # Si el dominio esta vacio, se informa de inmediato.
    if domain == "":
        print(f"{RED}[!] Debes ingresar un dominio valido.{RESET}")
        return

    # Si falta el protocolo, se agrega uno basico.
    url = domain
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        # Esta linea intenta conectarse a la pagina.
        response = requests.get(url, timeout=5)
    except requests.RequestException as error:
        # Si falla la peticion, mostramos el error.
        print(f"{RED}[!] Error al conectar: {error}{RESET}")
        return

    # Estas lineas muestran las cabeceras HTTP encontradas.
    print(f"\n{CYAN}[+] Encabezados HTTP para {url}:{RESET}\n")
    for header, value in response.headers.items():
        print(f"{YELLOW}{header}:{RESET} {value}")


def ping_y_os(target):
    # Si el objetivo viene vacio, detenemos la funcion.
    if target == "":
        print(f"{RED}[!] Debes ingresar un objetivo valido.{RESET}")
        return

    # Esta linea informa el inicio de la prueba.
    print(f"\n{CYAN}[+] Haciendo ping a {target} para deteccion de OS...{RESET}\n")

    # Esta variable adapta el parametro al sistema operativo.
    count_parameter = "-n" if platform.system() == "Windows" else "-c"

    try:
        # Esta linea ejecuta el ping y captura su salida.
        result = subprocess.run(
            ["ping", count_parameter, "4", target],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        # Si ping no existe, se informa al usuario.
        print(f"{RED}[!] El comando ping no esta disponible.{RESET}")
        return
    except Exception as error:
        # Este bloque informa errores inesperados.
        print(f"{RED}[!] Error en el ping: {error}{RESET}")
        return

    # Esta linea muestra la salida completa del comando.
    print(result.stdout)

    # Esta linea pasa la salida a minusculas para revisar el TTL.
    output = result.stdout.lower()

    # Si encontramos TTL de Windows, se informa al usuario.
    if "ttl=128" in output:
        print(f"{CYAN}[*] OS detectado de forma basica: Windows{RESET}")
        return

    # Si encontramos TTL de Linux o Unix, tambien se informa.
    if "ttl=64" in output:
        print(f"{CYAN}[*] OS detectado de forma basica: Linux o Unix{RESET}")
        return

    # Si no hay una coincidencia clara, se avisa.
    print(f"{YELLOW}[*] No fue posible inferir el sistema operativo con el TTL.{RESET}")


def mostrar_menu():
    # Estas lineas imprimen las opciones disponibles del programa.
    print(f"{GREEN}[1]{RESET} WHOIS Lookup")
    print(f"{GREEN}[2]{RESET} DNS Lookup y deteccion de OS")
    print(f"{GREEN}[3]{RESET} Deteccion de encabezados HTTP")
    print(f"{GREEN}[4]{RESET} Salir")


def main():
    # Este bucle mantiene vivo el menu hasta que el usuario quiera salir.
    while True:
        # Esta linea limpia la pantalla en cada vuelta.
        limpiar_pantalla()

        # Esta linea imprime el banner principal.
        mostrar_banner()

        # Esta linea muestra las opciones.
        mostrar_menu()

        # Esta linea pide la opcion del usuario.
        option = input(f"\n{MAGENTA}[?]{RESET} Selecciona una opcion: ").strip()

        # Este bloque maneja la opcion 1.
        if option == "1":
            domain = pedir_dominio(f"{CYAN}[>]{RESET} Dominio para WHOIS: ")
            whois_lookup(domain)
            pause()

        # Este bloque maneja la opcion 2.
        elif option == "2":
            domain = pedir_dominio(f"{CYAN}[>]{RESET} Dominio para DNS y OS: ")
            ip = dns_lookup(domain)
            if ip is not None:
                ping_y_os(ip)
            pause()

        # Este bloque maneja la opcion 3.
        elif option == "3":
            domain = pedir_dominio(f"{CYAN}[>]{RESET} Dominio para HTTP: ")
            detectar_banner_http(domain)
            pause()

        # Este bloque cierra el programa.
        elif option == "4":
            print(f"{YELLOW}[~] Until we meet again, Hacker...{RESET}")
            break

        # Cualquier valor fuera del menu se marca como invalido.
        else:
            print(f"{RED}[!] Opcion no valida.{RESET}")
            pause()


if __name__ == "__main__":
    # Esta condicion ejecuta la aplicacion solo cuando el archivo se corre directamente.
    main()
