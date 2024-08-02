import ssl
import socket

def check_ssl(hostname):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.do_handshake()
                print(f"{hostname} is secure (uses HTTPS).")
    except ssl.SSLError:
        print(f"{hostname} is not secure (does not use HTTPS).")

# Exemple d'utilisation
check_ssl("www.google.com")  # Exemple d'un site sécurisé
check_ssl("example.com")     # Exemple d'un site non sécurisé

# untrusted-root.badssl.com