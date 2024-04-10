import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_ecommerce_website_login():
    driver=Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://www.amazon.in/")
    driver.find_element(By.XPATH,"//span[text()='Account & Lists']").click()
    driver.find_element(By.ID,"ap_email").send_keys('9380191862')
    driver.find_element(By.ID,"continue").click()
    driver.find_element(By.ID,"ap_password").send_keys('Ganinaik123@')
    driver.find_element(By.ID,"signInSubmit").click()
    time.sleep(50)
    try:
        assert driver.find_element(By.XPATH,"//span[text()='Hello, Ganesh']").is_displayed()
        print("PASS:User can Login and User Account Name displayed in Home Page ")
    except:
        print("FAIL:User cannot  Login and User Account Name cannot displayed in Home Page")

def test_search_product():
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://www.amazon.in/")
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys("HP laptop")
    driver.find_element(By.ID,"twotabsearchtextbox").screenshot('search.png')
    driver.find_element(By.ID,"nav-search-submit-button").click()
    element=driver.find_element(By.XPATH,"(//a[@target='_blank'])[3]")
    actions=ActionChains(driver)
    actions.scroll_to_element(element).perform()
    element.click()
    product_text=driver.find_element(By.XPATH,"(//span[contains(.,'HP Envy x360, Enhanced by AI')])[3]").text
    print(product_text)
    product_price=driver.find_element(By.XPATH,"(//span[contains(.,'HP Envy x360, Enhanced by AI')])[3]/../../../..//span[@class='a-price-whole']").text
    print(product_price)
    time.sleep(5)


# def test_purchase_a_product():
#     driver = Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     driver.get("https://www.amazon.in/")
#     driver.find_element(By.ID,"twotabsearchtextbox").send_keys("HP laptop")
#     driver.find_element(By.ID, "nav-search-submit-button").click()
#     element = driver.find_element(By.XPATH, "(//a[@target='_blank'])[3]")
#     actions = ActionChains(driver)
#     actions.scroll_to_element(element).perform()
#     element.click()
#     driver.find_element(By.NAME,"submit.buy-now").click()
#     driver.find_element(By.ID,"orderSummaryPrimaryActionBtn-announce").click()





