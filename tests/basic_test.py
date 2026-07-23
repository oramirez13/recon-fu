import os
import socket
import sys
from unittest.mock import patch, MagicMock

import pytest

# Esta linea agrega la carpeta del proyecto al path para poder importar recon_fu.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from recon_fu import BASE_DIR, pedir_dominio, dns_lookup


# Este test verifica que BASE_DIR es una ruta absoluta.
def test_base_dir_is_absolute():
    assert os.path.isabs(BASE_DIR)


# Este test verifica que pedir_dominio valida entradas vacias.
@patch("builtins.input", return_value="")
def test_pedir_dominio_vacio(mock_input):
    result = pedir_dominio("Dominio: ")
    assert result == ""


# Este test verifica que pedir_dominio limpia espacios.
@patch("builtins.input", return_value="  example.com  ")
def test_pedir_dominio_limpia_espacios(mock_input):
    result = pedir_dominio("Dominio: ")
    assert result == "example.com"


# Este test verifica que dns_lookup retorna None con dominio vacio.
def test_dns_lookup_vacio():
    result = dns_lookup("")
    assert result is None


# Este test verifica que dns_lookup resuelve un dominio real.
def test_dns_lookup_real():
    result = dns_lookup("localhost")
    assert result is not None
    assert result == "127.0.0.1"


# Este test verifica que dns_lookup maneja dominios inexistentes.
def test_dns_lookup_inexistente():
    result = dns_lookup("noexiste12345abc.xyz")
    assert result is None


# Este test verifica que dns_lookup retorna IPv4.
@patch("socket.getaddrinfo")
def test_dns_lookup_retorna_ipv4(mock_getaddrinfo):
    # Se simula una respuesta de getaddrinfo con IPv4.
    mock_getaddrinfo.return_value = [
        (socket.AF_INET, socket.SOCK_STREAM, 0, "", ("93.184.216.34", 0)),
    ]
    result = dns_lookup("example.com")
    assert result == "93.184.216.34"


# Este test verifica que dns_lookup maneja multiples IPs.
@patch("socket.getaddrinfo")
def test_dns_lookup_multiples_ips(mock_getaddrinfo):
    # Se simula una respuesta con multiples direcciones.
    mock_getaddrinfo.return_value = [
        (socket.AF_INET, socket.SOCK_STREAM, 0, "", ("1.1.1.1", 0)),
        (socket.AF_INET, socket.SOCK_STREAM, 0, "", ("8.8.8.8", 0)),
    ]
    result = dns_lookup("example.com")
    assert result in ["1.1.1.1", "8.8.8.8"]
