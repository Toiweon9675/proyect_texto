import subprocess
from datetime import datetime

archivo = "prueba.txt"

# Escribir la fecha y hora actual en el archivo
with open(archivo, "w", encoding="utf-8") as f:
    f.write(f"Última actualización: {datetime.now()}\n")

print("Archivo actualizado")

# Configurar identidad del bot
subprocess.run(["git", "config", "user.email", "bot@example.com"])
subprocess.run(["git", "config", "user.name", "GitHub Actions Bot"])

# Commit y push
subprocess.run(["git", "add", archivo])
subprocess.run(["git", "commit", "-m", f"Actualización automática {datetime.now()}"])
subprocess.run(["git", "push"])

print("Cambios subidos a GitHub")
