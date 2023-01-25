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


driver.execute_script("window.scrollBy(0, 900);")
selenium_ruby = driver.find_element(By.CSS_SELECTOR, "[data-product_id='160']")
selenium_ruby.click()

driver.execute_script("window.scrollBy(0, 600);")
reviews = driver.find_element(By.CSS_SELECTOR, ".tabs.wc-tabs > li:nth-child(2)")
reviews.click()

driver.execute_script("window.scrollBy(0, 200);")
stars_5 = driver.find_element(By.CLASS_NAME, "star-5")
stars_5.click()

driver.execute_script("window.scrollBy(0, 200);")
comment_f = driver.find_element(By.ID, "comment")
comment_f.send_keys("Nice book!")
name_f = driver.find_element(By.ID, "author")
name_f.send_keys("Oleg")
email_f = driver.find_element(By.ID, "email")
email_f.send_keys("1@gmail.com")
submit_btn = driver.find_element(By.CLASS_NAME, "submit")
submit_btn.click()

driver.quit()