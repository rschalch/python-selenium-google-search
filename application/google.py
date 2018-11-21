import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_driver():
    return webdriver.Firefox()


def get_results(driver, term):
    driver.get('http://www.google.com')

    search = driver.find_element_by_name('q')
    search.send_keys(term)
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    links = driver.find_elements_by_css_selector('h3.LC20lb')

    results = []

    for i in range(3):
        results.append(links[i].text)

    return results


