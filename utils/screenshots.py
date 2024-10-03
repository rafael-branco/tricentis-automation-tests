import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    folder_path = "screenshots/"
    os.makedirs(folder_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{folder_path}{name}_{timestamp}.png"
    driver.save_screenshot(file_path)