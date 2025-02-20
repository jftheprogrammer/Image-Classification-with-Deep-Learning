import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # File handler with log rotation
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, "app.log"), maxBytes=1024 * 1024, backupCount=5
    )
    file_handler.setFormatter(logging.Formatter(log_format))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    
    # Root logger
    logging.basicConfig(
        level=logging.INFO, handlers=[file_handler, console_handler]
    )