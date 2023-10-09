from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.get("https://3dwarehouse.sketchup.com/search/products")

try:
    wait = WebDriverWait(driver, 60)
    
    div = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'profile-header__username')))
    
    if div:
        cookies = driver.get_cookies()
        pickle.dump(cookies, open("cookies.pkl", "wb"))
    
except Exception as e:
    print("Error:", str(e))

finally:
    driver.quit()
