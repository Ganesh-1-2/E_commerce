import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_ecommerce_website_login():
    # test case for automation login
    driver=Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://www.amazon.in/")
    driver.find_element(By.XPATH,"//span[text()='Account & Lists']").click()
    driver.find_element(By.ID,"ap_email").send_keys('9380191862')
    driver.find_element(By.ID,"continue").click()
    driver.find_element(By.ID,"ap_password").send_keys('Ganinaik123@')
    driver.find_element(By.ID,"signInSubmit").click()
    driver.find_element(By.XPATH,"//input[@type='tel']").click()
    time.sleep(20)
    driver.find_element(By.XPATH,"//span[text()='Submit code']").submit()
    # sometimes application asks for otp or CAPTCHA. that moment we cant automate the application. so we can take above (comment out) code. that time we can give the otp value manually
    try:
        assert driver.find_element(By.XPATH,"//span[text()='Hello, Ganesh']").is_displayed()
        print("PASS:User can Login and User Account Name displayed in Home Page ")
    except:
        print("FAIL:User cannot  Login and User Account Name cannot displayed in Home Page")

def test_search_product():
    # test automation code for search a product
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://www.amazon.in/")
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile cover")
    driver.find_element(By.ID, "twotabsearchtextbox").screenshot('search_product.png')
    driver.find_element(By.ID,"nav-search-submit-button").click()
    element=driver.find_element(By.XPATH,"//span[contains(text(),'Solimo Plastic Mobile Cover')]")
    actions=ActionChains(driver)
    actions.scroll_to_element(element).perform()
    element.click()
    time.sleep(5)

def test_text_and_price_of_product():
    # test automation code for the text and price of the product
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://www.amazon.in/")
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile cover")
    driver.find_element(By.ID, "twotabsearchtextbox").screenshot('search_product.png')
    driver.find_element(By.ID,"nav-search-submit-button").click()
    element=driver.find_element(By.XPATH,"//span[contains(text(),'Solimo Plastic Mobile Cover')]")
    actions=ActionChains(driver)
    actions.scroll_to_element(element).perform()
    element.click()
    product_text = driver.find_element(By.XPATH, "(//span[contains(text(),'Solimo Plastic Mobile Cover')])[1]").text
    print(product_text)
    product_price=driver.find_element(By.XPATH,"(//span[contains(text(),'Solimo Plastic Mobile Cover')]/../../../..//span[@class='a-price-whole'])[1]").text
    print(product_price)
    time.sleep(2)







