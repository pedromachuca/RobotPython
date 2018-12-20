# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
#from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()

print ">Connecting.."
browser.get("https://www.hackthis.co.uk/") # Load page

print ">Logining.."
username = "pedromachuka"
loginForm = browser.find_element_by_name("username")
loginForm.send_keys(username.decode("utf-8"))

password = "8caractere"
passwordForm = browser.find_element_by_name("password")
passwordForm.send_keys(password)

submit = browser.find_element_by_class_name("button")
submit.click()

print ">Go to page.."
browser.get("https://www.hackthis.co.uk/levels/coding/1")

now = time.time()

print ">Sourse code"
page_sourse = BeautifulSoup(browser.page_source, "lxml")
string = str(page_sourse.findAll('textarea')[0].contents[0].decode("utf-8"))
data = string.split(", ")

print ">Input: " + str(len(data))
print string

data.sort()
result = ', '.join(data)

print ">Result: " + str(len(data))
print result

print ">Sending answer.."
answer = browser.find_element_by_name("answer")
answer.send_keys(result.encode("utf-8"))

fsubmit = browser.find_element_by_xpath("//input[@type='submit']")
fsubmit.click()

print ">Finished!"

later = time.time()
difference = int(later - now)

print "It has been :%d seconds"%difference

