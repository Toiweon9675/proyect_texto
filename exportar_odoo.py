import subprocess
from datetime import datetime

archivo = "prueba.txt"

# Abrir en modo append para ACUMULAR
with open(archivo, "a", encoding="utf-8") as f:
    f.write(f"Actualización automática: {datetime.now()}\n")

# Configurar identidad de Git
subprocess.run(["git", "config", "user.email", "bot@example.com"])
subprocess.run(["git", "config", "user.name", "GitHub Actions Bot"])

# Añadir cambios
subprocess.run(["git", "add", archivo])

# Commit con mensaje único
subprocess.run(["git", "commit", "-m", f"Actualización automática {datetime.now()}"])

# Push
subprocess.run(["git", "push"])
