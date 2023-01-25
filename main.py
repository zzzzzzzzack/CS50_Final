import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# add path for selenium drivers for chrome browser

def main():
    # Add options to allow the chrome browser to stay open
    os.environ['PATH'] += r"C:\Users\19zac\SeleniumChromeDrivers"
    options = webdriver.ChromeOptions()
    # Set the driver options so the window stays open
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver.maximize_window()

    # Open desired link
    driver.get("https://www.w3schools.com/html/html_forms.asp")
    driver.implicitly_wait(3)

    # link_element = driver.find_element("id", "block-easy-breadcrumb-easy-breadcrumb")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[3]/div/form/input[3]")))
    # driver.find_element(By.XPATH, "/html/body/form/input[3]")
    # main_element = driver.find_element(By.ID, "iframeResult")
    # input_buttons = main_element.find_elements(By.TAG_NAME, "input")
    form = "/html/body/div[7]/div[1]/div[1]/div[3]/div/form/"

    input_first_name = driver.find_element(By.XPATH, form + "input[1]")
    input_first_name.clear()
    input_first_name.send_keys("Zack")

    input_last_name = driver.find_element(By.XPATH, form + "input[2]")
    input_last_name.clear()
    input_last_name.send_keys("Moore")

    input_button = driver.find_element(By.XPATH, form + "input[3]")
    input_button.click()

    # for input in input_buttons:
    #     print("input is %s", input.get_attribute("value"))
    #     input.click()


if __name__ == "__main__":
    main()