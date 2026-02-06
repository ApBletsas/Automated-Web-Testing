import os
import json
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# -------------------------
# LOGGING SETUP
# -------------------------
LOG_FILE = "logs/test_login.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------
# LOAD CONFIG
# -------------------------
with open("config.json") as f:
    config = json.load(f)

# -------------------------
# MAIN TEST FUNCTION
# -------------------------
def run_test(test_config):
    logging.info(f"Starting login test: {test_config['name']}")

    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(test_config["url"])

    try:
        # Fill in username
        username_field = WebDriverWait(driver, test_config["wait_time"]).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(test_config["username"])

        # Fill in password
        password_field = WebDriverWait(driver, test_config["wait_time"]).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(test_config["password"])
        password_field.send_keys(Keys.RETURN)

        # Wait for success message
        success_message = WebDriverWait(driver, test_config["wait_time"]).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )

        if "You logged into a secure area!" in success_message.text:
            logging.info(f"{test_config['name']} test PASSED")
        else:
            logging.warning(f"{test_config['name']} test FAILED")

    except TimeoutException as e:
        logging.error(f"{test_config['name']} timeout waiting for element: {e}")
    except NoSuchElementException as e:
        logging.error(f"{test_config['name']} element not found: {e}")
    except Exception as e:
        logging.error(f"{test_config['name']} unexpected error: {e}")
    finally:
        driver.quit()
        logging.info(f"{test_config['name']} login test completed")

# -------------------------
# ENTRY POINT
# -------------------------
if __name__ == "__main__":
    for test in config["tests"]:
        run_test(test)