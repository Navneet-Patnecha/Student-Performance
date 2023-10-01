import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
log_path = os.path.join(os.getcwd(), "logs" , LOG_FILE)
os.makedirs(log_path,exist_ok=True)
