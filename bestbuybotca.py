import bs4
import sys
import time
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.webdriver import FirefoxProfile

# Twilio configuration (Optional)
toNumber = 'your_phonenumber'
fromNumber = 'twilion_phonenumber'
accountSid = 'ssid'
authToken = 'authToken'
client = Client(accountSid, authToken)

# Product Page (By default, This URL will scan all RTX Founder Edition's at one time (3060ti and 3070.)
url = 'https://www.bestbuy.ca/en-ca/search?path=brandName%253ANVIDIA%253Bsoldandshippedby0enrchstring%253ABest%2BBuy&search=rtx'
# Please do not use URL of a Specific Product like the example URL below.
# https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3070-8gb-gddr6-video-card-only-at-best-buy/15078017
# If you are only interested in a specific graphics card. Use a URL link like this instead.
# You'll see how I used bestbuy filters on website to only show a specific card on the URL below.
# https://www.bestbuy.ca/en-ca/collection/rtx-30-series-graphic-cards/316108?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcurrentoffers0enrchstring%253ABest%2BBuy%2BExclusive

def timeSleep(x, driver):
    for i in range(x, -1, -1):
        sys.stdout.write('\r')
        sys.stdout.write('{:2d} seconds'.format(i))
        sys.stdout.flush()
        time.sleep(1)
    driver.refresh()
    sys.stdout.write('\r')
    sys.stdout.write('Page refreshed\n')
    sys.stdout.flush()


def createDriver():
    """Creating driver."""
    options = Options()
    options.headless = False  # Change To False if you want to see Firefox Browser Again.
    profile = webdriver.FirefoxProfile(r'C:\Users\Hououin Kyouma\AppData\Roaming\Mozilla\Firefox\Profiles\54d2m725.default-release')
    driver = webdriver.Firefox(profile, options=options, executable_path=GeckoDriverManager().install())
    return driver


def driverWait(driver, findType, selector):
    """Driver Wait Settings."""
    while True:
        if findType == 'css':
            try:
                driver.find_element_by_css_selector(selector).click()
                break
            except NoSuchElementException:
                driver.implicitly_wait(0.2)
        elif findType == 'name':
            try:
                driver.find_element_by_name(selector).click()
                break
            except NoSuchElementException:
                driver.implicitly_wait(0.2)

def findingCards(driver):
    """Scanning all cards."""
    driver.get(url)
    while True:
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, 'html.parser')
        wait = WebDriverWait(driver, 10)
        wait2 = WebDriverWait(driver, 2)
        try:
            time.sleep(.5)
            findAllCards = soup.find('span', {'data-automation': 'store-availability-checkmark'})
            if findAllCards:
                print(f'Button Found!: {findAllCards.get_text()}')

                # Clicking Item.
                time.sleep(3)
                driverWait(driver, 'css', '.shippingAvailability_2RMa1')
                time.sleep(1)

                # Clicking Add to Cart.
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button_2m0Gt primary_RXOwf addToCartButton_1op0t addToCartButton regular_23pTm']")))
                    time.sleep(2)
                    driver.find_element_by_xpath("//button[@class='button_2m0Gt primary_RXOwf addToCartButton_1op0t addToCartButton regular_23pTm']").click()
                    print("Added to Cart")
                except (NoSuchElementException, TimeoutException):
                    print("Error Add To Cart")
                    timeSleep(3, driver)
                    findingCards(driver)
                    return

                # Going To Cart.
                time.sleep(2)
                driver.get('https://www.bestbuy.ca/en-ca/basket')
                time.sleep(2)

                # Click Go to Checkout
                time.sleep(2)
                driver.get('https://www.bestbuy.ca/identity/global/signin?redirectUrl=https%3A%2F%2Fwww.bestbuy.ca%2Fcheckout%2F%3Fqit%3D1%23%2Fen-ca%2Fshipping%2FON%2FK1L%206A7&amp;lang=en-CA&amp;contextId=checkout')
                time.sleep(2)

                # Logging Into Account.
                print("Attempting to Login.")
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='_3PA_N _3eMWM signin-form-button _2_yQI owsdg']")))
                    time.sleep(2)
                    driver.find_element_by_xpath("//button[@class='_3PA_N _3eMWM signin-form-button _2_yQI owsdg']").click()
                    print("Login Successful")
                except (NoSuchElementException, TimeoutException):
                    pass

                # Click Shipping Option. (If Available)
                try:
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fulfillment_1losStandard0")))
                    time.sleep(1)
                    driverWait(driver, 'css', '#fulfillment_1losStandard0')
                    print("Clicking Shipping Option.")
                except (NoSuchElementException, TimeoutException):
                    pass

                # Trying CVV
                try:
                    print("\nTrying CVV Number.\n")
                    security_code = driver.find_element_by_id("cvv")
                    time.sleep(1)
                    security_code.send_keys("123")  # You can enter your CVV number here.
                except (NoSuchElementException, TimeoutException):
                    pass

                # Bestbuy Text Updates.
                try:
                    wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#text-updates")))
                    driverWait(driver, 'css', '#text-updates')
                    print("Selecting Text Updates.")
                except (NoSuchElementException, TimeoutException):
                    pass

                # Final Checkout.
                try:
                    wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-now")))
                    driverWait(driver, 'css', '.order-now')
                except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
                    try:
                        wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".primary_1oCqK ")))
                        driverWait(driver, 'css', '.primary_1oCqK ')
                        timeSleep(5, driver)
                        wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-now")))
                        time.sleep(1)
                        driverWait(driver, 'css', '.order-now')
                    except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
                        print("Could Not Complete Checkout.")

                # Completed Checkout.
                print('Order Placed!')
                try:
                    client.messages.create(to=toNumber, from_=fromNumber, body='ORDER PLACED!')
                except (NameError, TwilioRestException):
                    pass
                for i in range(3):
                    print('\a')
                    time.sleep(1)
                time.sleep(1)
                driver.quit()
                return
            else:
                pass

        except NoSuchElementException:
            pass
        timeSleep(5, driver)


if __name__ == '__main__':
    driver = createDriver()
    findingCards(driver)
