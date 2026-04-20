import shutil
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s")
origen  = "origen/ventas.csv"
destino = "data/raw/ventas.csv"

logging.info("Inicio del proceso de ingesta")

try:
    shutil.copy(origen, destino)
    logging.info(f"Archivo copiado correctamente: {destino}")
except FileNotFoundError:
    logging.error(f"Archivo origen no encontrado: {origen}")
except Exception as e:
    logging.error(f"Error en la ingesta: {e}")
    
