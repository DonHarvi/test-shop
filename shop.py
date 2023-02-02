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
# login_f = driver.find_element(By.ID, "username")
# login_f.send_keys("toprba@gmail.com")
# password_f = driver.find_element(By.ID, "password")
# password_f.send_keys("!Selenium1!")
# login_btn = driver.find_element(By.CSS_SELECTOR, "[name=login]")
# login_btn.click()
#
# shop_menu = driver.find_element(By.ID, "menu-item-40")
# shop_menu.click()
#
# html5 = driver.find_element(By.CSS_SELECTOR, "[title='Mastering HTML5 Forms']")
# html5.click()
#
# h1_title = driver.find_element(By.TAG_NAME, "h1").text
# if h1_title in "HTML5 Forms":
#     print(f"Title of the book is {h1_title}")
# else: print("SMTH WRONG!")
#
# driver.quit()


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
# login_f = driver.find_element(By.ID, "username")
# login_f.send_keys("toprba@gmail.com")
# password_f = driver.find_element(By.ID, "password")
# password_f.send_keys("!Selenium1!")
# login_btn = driver.find_element(By.CSS_SELECTOR, "[name=login]")
# login_btn.click()
#
# shop_menu = driver.find_element(By.ID, "menu-item-40")
# shop_menu.click()
#
# html_menu = driver.find_element(By.CSS_SELECTOR, ".cat-item.cat-item-19 > a")
# html_menu.click()
# html_count = driver.find_elements(By.CLASS_NAME, "products.masonry-done > li")
# assert(len(html_count)) == 3
#
# print("It's OK")
#
# driver.quit()


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
# login_f = driver.find_element(By.ID, "username")
# login_f.send_keys("toprba@gmail.com")
# password_f = driver.find_element(By.ID, "password")
# password_f.send_keys("!Selenium1!")
# login_btn = driver.find_element(By.CSS_SELECTOR, "[name=login]")
# login_btn.click()
#
# shop_menu = driver.find_element(By.ID, "menu-item-40")
# shop_menu.click()
#
# sort_box = driver.find_element(By.CSS_SELECTOR, "[value='menu_order']").get_attribute("selected")
# assert sort_box == "true"
#
# high_price_sort = driver.find_element(By.CSS_SELECTOR, ".orderby > option:nth-child(6)")
# high_price_sort.click()
#
# sort_box1 = driver.find_element(By.CSS_SELECTOR, "[value='price-desc']").get_attribute("selected")
# assert  sort_box1 == "true"
#
# driver.quit()

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
# login_f = driver.find_element(By.ID, "username")
# login_f.send_keys("toprba@gmail.com")
# password_f = driver.find_element(By.ID, "password")
# password_f.send_keys("!Selenium1!")
# login_btn = driver.find_element(By.CSS_SELECTOR, "[name=login]")
# login_btn.click()
#
# shop_menu = driver.find_element(By.ID, "menu-item-40")
# shop_menu.click()
#
# android_book  = driver.find_element(By.CSS_SELECTOR, "[title='Android Quick Start Guide']")
# android_book.click()
#
# old_price = driver.find_element(By.CSS_SELECTOR, ".price > del > span").text
# assert old_price == "₹600.00"
# new_price = driver.find_element(By.CSS_SELECTOR, ".price > ins > span").text
# assert new_price == "₹450.00"
#
# cover_img = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                                                        "[title='Android Quick Start Guide']")))
# cover_img.click()
# close_cover = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_cover.click()
#
# driver.quit()

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
# login_f = driver.find_element(By.ID, "username")
# login_f.send_keys("toprba@gmail.com")
# password_f = driver.find_element(By.ID, "password")
# password_f.send_keys("!Selenium1!")
# login_btn = driver.find_element(By.CSS_SELECTOR, "[name=login]")
# login_btn.click()
#
# shop_menu = driver.find_element(By.ID, "menu-item-40")
# shop_menu.click()
#
# cart_html5_book  = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# cart_html5_book.click()
#
# cart_btn = driver.find_element(By.CLASS_NAME, "cartcontents")
# cart_btn.click()
#
# subtotal = driver.find_element(By.CSS_SELECTOR, ".cart-subtotal > td > span").text
# assert subtotal is not None
# total = driver.find_element(By.CSS_SELECTOR, ".order-total > td > strong > span").text
# assert total is not None
#
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
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
# login_f = driver.find_element(By.ID, "username")
# login_f.send_keys("toprba@gmail.com")
# password_f = driver.find_element(By.ID, "password")
# password_f.send_keys("!Selenium1!")
# login_btn = driver.find_element(By.CSS_SELECTOR, "[name=login]")
# login_btn.click()
#
# shop_menu = driver.find_element(By.ID, "menu-item-40")
# shop_menu.click()
#
# driver.execute_script("window.scrollBy(0, 300);")
# cart_html5_book  = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# cart_html5_book.click()
# time.sleep(3)
# data_book = driver.find_element(By.CSS_SELECTOR, "[data-product_id='165']")
# data_book.click()
#
# cart_btn = driver.find_element(By.CLASS_NAME, "cartcontents")
# cart_btn.click()
# time.sleep(3)
#
# remove_book_1 = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
# remove_book_1.click()
#
# undo_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Undo?")
# undo_link.click()
# q_book_2 = driver.find_element(By.CSS_SELECTOR,
#                                       "[name='cart[4c5bde74a8f110656874902f07378009][qty]']").clear()
# q_book_21 = driver.find_element(By.CSS_SELECTOR,
#                                       "[name='cart[4c5bde74a8f110656874902f07378009][qty]']")
# q_book_21.click()
# driver.execute_script("arguments[0].setAttribute('value', arguments[1])", q_book_21, '3')
#
# update_btn = driver.find_element(By.CSS_SELECTOR, "[name=update_cart]")
# update_btn.click()
# time.sleep(3)
#
# apply_coupon = driver.find_element(By.CSS_SELECTOR, "[name=apply_coupon]")
# apply_coupon.click()
# time.sleep(3)
# error_message = driver.find_element(By.CSS_SELECTOR, ".page-content.entry-content > .woocommerce > .woocommerce-error")
# error_message_text = error_message.text
# assert error_message_text == "Please enter a coupon code."
#
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

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

shop_menu = driver.find_element(By.ID, "menu-item-40")
shop_menu.click()

driver.execute_script("window.scrollBy(0, 300);")
cart_html5_book  = driver.find_element(By.CSS_SELECTOR, "[data-product_id='165']")
cart_html5_book.click()
time.sleep(2)
cart_btn = driver.find_element(By.CLASS_NAME, "cartcontents")
cart_btn.click()

driver.execute_script("window.scrollBy(0, 300);")
checkout_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                                           "checkout-button.button.alt.wc-forward"))).click()

first_name = driver.find_element(By.ID, "billing_first_name")
first_name.send_keys("Oleg")
last_name = driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Olegov")
email_f = driver.find_element(By.ID, "billing_email")
email_f.send_keys("1@gmail.com")
phone = driver.find_element(By.ID, "billing_phone")
phone.send_keys("89111232323")


driver.execute_script("window.scrollBy(0, 300);")
country_s = driver.find_element(By.ID, "billing_country_field").click()
country_f = driver.find_element(By.ID, "s2id_autogen1_search")
country_f.send_keys("india")
india_c = driver.find_element(By.CSS_SELECTOR, ".select2-results > li:nth-child(2)").click()

address = driver.find_element(By.ID, "billing_address_1")
address.send_keys("Olegova")
city = driver.find_element(By.ID, "billing_city")
city.send_keys("LA")

driver.execute_script("window.scrollBy(0, 300);")
state = driver.find_element(By.ID, "s2id_billing_state").click()
time.sleep(10)
state_f = driver.find_element(By.ID, "s2id_autogen2_search")
state_f.send_keys("as")
assam = driver.find_element(By.CSS_SELECTOR, ".select2-results > li:nth-child(1)").click()
time.sleep(5)

zip = driver.find_element(By.ID, "billing_postcode")
zip.send_keys("1232345")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check_pay = driver.find_element(By.ID, "payment_method_cheque")
check_pay.click()

order_btn = driver.find_element(By.ID, "place_order")
order_btn.click()

driver.quit()