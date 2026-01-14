import logging
import sys
from pathlib import Path

log_dir = Path("logs")
log_filepath = log_dir / "etl.log"

def setup_custom_logger(name: str):

    log_format = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)

    file_handler = logging.FileHandler(log_filepath, mode='a', encoding='utf-8')
    file_handler.setFormatter(log_format)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger