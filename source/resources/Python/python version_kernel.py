# Ejecutar en terminal "python version_kernel.py"

import os

def obtener_version_kernel():
    # Ejecutar el comando "uname -r" en el terminal y capturar la salida usando el módulo os
    resultado = os.popen('uname -r').read().strip()
    return resultado

if __name__ == "__main__":
    version_kernel = obtener_version_kernel()
    print(f"La versión del kernel es: {version_kernel}")

