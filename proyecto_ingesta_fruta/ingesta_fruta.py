import shutil
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s")
origen  = "origen/ventas.csv"
destino = "data/raw/ventas.csv"

logging.info("Inicio del proceso de ingesta")

try:
    shutil.copy(origen, destino)
    logging.info(f"Archivo copiado correctamente: {destino}")
except FileNotFoundError:
    logging.error(f"Archivo no encontrado: {origen}")

