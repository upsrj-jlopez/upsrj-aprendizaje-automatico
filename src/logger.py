import sys
import logging
from config import get_log_file

def set_logger(file_path: str = 'app.log', level: str = logging.DEBUG,
               format: str = "%(asctime)s [%(levelname)s] %(message)s") -> None:
    logging.basicConfig(
        level=level,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
        format=format,
        handlers=[
            logging.FileHandler(get_log_file(file_path), mode='w', encoding="utf-8")
        ]
    )

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)

def plogger(msg: str = '', level: str = logging.INFO) -> None:
    if   level == logging.INFO:    logging.info(msg)
    elif level == logging.DEBUG:   logging.debug(msg)
    elif level == logging.WARNING: logging.warning(msg)
    elif level == logging.ERROR:   logging.error(msg)
    print(msg)