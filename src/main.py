# ============================================================
# Politécnica de Santa Rosa
#
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: [nombre_del_archivo.py]
# Descripción: [breve descripción del propósito del archivo]
# ============================================================
import sys, os
from logger import set_logger, get_logger, plogger
from logging import DEBUG, INFO, WARNING, ERROR

set_logger(file_path=__file__)
logger = get_logger(__name__)

def main():
    try:
        logger.info("Iniciando programa...")
        plogger("Hello World!")

    except OSError as e:
        plogger(f"OSError [{e.errno}]: {os.strerror(e.errno)}", level=ERROR)
        return os.EX_SOFTWARE

    except Exception:
        logger.exception("Error inesperado")
        return os.EX_SOFTWARE

    logger.info("Programa finalizado correctamente.")
    return os.EX_OK

if __name__ == "__main__":
    sys.exit(main())