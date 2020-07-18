import time

from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("http://www.google.com")

driver.find_element_by_name("q").send_keys("automation step by step")

time.sleep(5)

driver.find_elements_by_class_name("gNO89b")


time.sleep(5)

driver.close()

driver.quit()

print("test completed")