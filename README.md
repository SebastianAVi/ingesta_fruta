# 🍎 Ingesta de Datos - Ventas de Fruta

Proyecto de **pipeline de ingesta de datos** para procesar ventas de productos de fruta.

## 📋 Descripción

Este proyecto implementa un proceso simple pero estructurado de **ingesta de datos**, copiando un archivo de ventas desde una carpeta de origen (`origen/`) hacia la capa `raw` del data lake (`data/raw/`).

Es un ejemplo ideal para demostrar conceptos básicos de **Data Engineering**:
- Organización de carpetas en un Data Lake
- Logging de procesos
- Manejo de errores
- Pipelines de ingesta

## 🏗️ Estructura del Proyecto

```bash
ingesta_fruta/
├── proyecto_ingesta_fruta/
│   ├── ingesta_fruta.py          # Script principal de ingesta
│   ├── origen/
│   │   └── ventas.csv            # Fuente original de datos
│   └── data/
│       └── raw/
│           └── ventas.csv        # Datos en capa Raw (después de la ingesta)
├── README.md
└── .gitignore
📊 Datos
El archivo ventas.csv contiene información de ventas de frutas con la siguiente estructura:






























ColumnaTipoDescripciónidIntegerIdentificador de ventaproductoStringNombre de la frutacantidadIntegerCantidad vendidaprecioIntegerPrecio unitario
Ejemplo de datos:
csvid,producto,cantidad,precio
1,Manzana,150,1200
2,Naranja,80,950
3,Platano,200,600
🚀 Cómo ejecutar
1. Clonar el repositorio
Bashgit clone https://github.com/SebastianAVi/ingesta_fruta.git
cd ingesta_fruta/proyecto_ingesta_fruta
2. Ejecutar el script de ingesta
Bashpython ingesta_fruta.py
3. Ver resultado
El archivo ventas.csv se copiará desde origen/ a data/raw/.
📝 Logs
El script genera logs informativos en consola:

Inicio del proceso
Confirmación de copia exitosa
Errores en caso de que el archivo no exista

🛠️ Tecnologías utilizadas

Python 3
shutil (para copiar archivos)
logging (para registro de eventos)
Estructura de carpetas tipo Data Lake (Raw layer)

📌 Próximos pasos (posibles mejoras)

Agregar validaciones de datos
Implementar ingesta incremental
Agregar carga a capa Processed
Convertir en DAG de Airflow o script programado
Añadir tests unitarios
Dockerizar el proceso
