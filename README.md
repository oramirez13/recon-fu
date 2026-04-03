# REC ON FU - Infra & Web Reconnaissance

REC ON FU es un módulo avanzado de recolección de información desarrollado en Python. Forma parte del ecosistema `CTF-Toolkit` y está diseñado para realizar una fase de reconocimiento (Footprinting) rápida y efectiva sobre objetivos en red local o dominios externos.

---

## Características Principales

* **WHOIS Lookup**: Consulta datos de registro, fechas de expiración y proveedores de dominios.
* **DNS & OS Fingerprinting**: Resuelve nombres de dominio a IP y analiza el valor TTL (Time To Live) del host para identificar si el objetivo es un sistema **Windows** o **Linux/Unix**.
* **Banner Grabbing HTTP**: Recupera y analiza los encabezados de respuesta del servidor para identificar el software (Apache, Nginx, IIS), versiones y posibles configuraciones de seguridad.
* **Interfaz Dinámica**: Utiliza arte ASCII generado en tiempo real y códigos de colores ANSI para una mejor experiencia en la terminal.

---

## Captura de Interfaz

```text
██████╗ ███████╗ ██████╗    ██████╗ ███╗   ██╗    ███████╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝   ██╔═══██╗████╗  ██║    ██╔════╝██║   ██║
██████╔╝█████╗  ██║        ██║   ██║██╔██╗ ██║    █████╗  ██║   ██║
██╔══██╗██╔══╝  ██║        ██║   ██║██║╚██╗██║    ██╔══╝  ██║   ██║
██║  ██║███████╗╚██████╗   ╚██████╔╝██║ ╚████║    ██║     ╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═════╝ ╚═╝  ╚═══╝    ╚═╝      ╚═════╝ 
            REC ON FU – orami 2025

[1] WHOIS Lookup
[2] DNS Lookup & Detección de OS
[3] Detección de banner HTTP
[4] Salir
```

---

## Instalación y Uso

Se recomienda el uso de un entorno virtual para evitar conflictos con las librerías del sistema en distribuciones como Arch Linux.

```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar herramienta
python recon_fu.py
```

---

## Requisitos del Sistema
* Python 3.10+
* Conectividad a Internet (para WHOIS y DNS externos).

---

## Autor
**ORAMI (2025)** Estudiante de Ciberseguridad | Desarrollo Web
```
