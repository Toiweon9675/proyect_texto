import subprocess
from datetime import datetime

# Nombre del archivo que quieres actualizar
archivo = "prueba.txt"

# 1. Escribir SIEMPRE contenido nuevo (fecha/hora actual)
with open(archivo, "w", encoding="utf-8") as f:
    f.write(f"Última actualización automática: {datetime.now()}\n")

# 2. Configurar identidad de Git (necesario en GitHub Actions)
subprocess.run(["git", "config", "user.email", "bot@example.com"])
subprocess.run(["git", "config", "user.name", "GitHub Actions Bot"])

# 3. Añadir cambios
subprocess.run(["git", "add", archivo])

# 4. Hacer commit SIEMPRE con mensaje único
subprocess.run(["git", "commit", "-m", f"Actualización automática {datetime.now()}"])

# 5. Hacer push al repositorio
subprocess.run(["git", "push"])
