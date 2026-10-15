from pathlib import Path

# Para un determinado archivo
archivoPrueba = Path('mi_archivo.exe')
print(archivoPrueba.suffix.lstrip('.'))

# Para el script actual
rutaActual = Path(__file__).resolve().suffix.lstrip('.')
print(rutaActual)