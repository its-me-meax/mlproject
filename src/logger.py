
import logging
import os
from datetime import datetime

## Step 1: Create only the folder path
logs_dir = os.path.join(os.getcwd(), "logs")

# If "logs" exists and is a file, delete or rename it
if os.path.isfile(logs_dir):
    os.remove(logs_dir)

os.makedirs(logs_dir, exist_ok=True)


## Step 2: Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

## Step 3: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
