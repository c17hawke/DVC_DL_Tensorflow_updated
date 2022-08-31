import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO, format=logging_str,
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'running_logs.log')),#, mode="a"),
        logging.StreamHandler(sys.stdout)
    ])