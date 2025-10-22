import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

def setup_logging(enable_logging=True):
    """Initialize the logging system for the Flask app."""

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove default handlers if any
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    if not enable_logging:
        # Simulate missing logging/monitoring (OWASP A9)
        null_handler = logging.NullHandler()
        logger.addHandler(null_handler)
        return logger

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
    )

    # File handler (rotating logs)
    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Logging initialized.")
    return logger
