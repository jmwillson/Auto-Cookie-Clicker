from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
action = ActionChains(driver)

#Get cookie location
def cookie_location():
    driver.get('http://orteil.dashnet.org/cookieclicker/')
    element = driver.find_element_by_id("cookieAnchor")
    location = element.location
    return location

def move_mouse_and_click(driver):
    cookie = driver.find_element_by_id("cookieAnchor")
    action.move_to_element(cookie).perform()
    auto_click(cookie)

def auto_click(cookie):
    counter = 0
    while True:
        cookie.click()
        counter+=1
        print("Cookie's Clicked: " + str(counter))
        if (counter%1000 == 0):
            time.sleep(10)

def main():
    coord = cookie_location()
    time.sleep(2)
    move_mouse_and_click(driver)

if __name__ == '__main__':
    main()
