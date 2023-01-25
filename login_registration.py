# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'/Users/olga.tcyvian/Library/Application Support/Google/Chrome/Profile 2/Extensions/gighmmpiobklfepjocnamgkkbiglidom/5.3.3_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
#
# driver.get("https://practice.automationtesting.in/")
#
# my_account_menu = driver.find_element(By.ID, "menu-item-50")
# my_account_menu.click()
#
# reg_email = driver.find_element(By.ID, "reg_email")
# reg_email.send_keys("toprba@gmail.com")
# reg_password = driver.find_element(By.ID, "reg_password")
# reg_password.send_keys("!Selenium1!")
# submit_btn = driver.find_element(By.CSS_SELECTOR, ".woocomerce-FormRow.form-row > input:nth-child(3)")
# submit_btn.click()
#
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

path_to_extension = r'/Users/olga.tcyvian/Library/Application Support/Google/Chrome/Profile 2/Extensions/gighmmpiobklfepjocnamgkkbiglidom/5.3.3_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)

driver.get("https://practice.automationtesting.in/")

my_account_menu = driver.find_element(By.ID, "menu-item-50")
my_account_menu.click()

login_f = driver.find_element(By.ID, "username")
login_f.send_keys("toprba@gmail.com")
password_f = driver.find_element(By.ID, "password")
password_f.send_keys("!Selenium1!")
login_btn = driver.find_element(By.CSS_SELECTOR, "[name=login]")
login_btn.click()

if driver.find_element(By.CLASS_NAME,
                                  "woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout"):
    print("Logout exists on the page")

driver.quit()