# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
#from selenium.webdriver.support.ui import WebDriverWait

#fonction pour déchiffrer exercice
def sort(string):
    string = string.split(",")
    for i in range(len(string)):
        if(string[i]==" "):
            string[i]=0
        else:
            string[i]=int(string[i])
    for item in string:
        print(item) 
        print '\n'

#First step - 32
    for i in range(len(string)):
        string[i]=string[i]-32
    for item in string:
        print(item)
        print '\n'
        
#Second step original position
    for i in range(len(string)):
        string[i]=94-string[i]
    for item in string:
        print(item)
#Third step original ascii code
    for i in range(len(string)):
        string[i]=string[i]+32

#Last step original ascii code to Char
    for i in range(len(string)):
        if(string[i]==158):
            string[i]=chr(32)
        else:
            string[i]=chr(string[i])
    for item in string:
        print(item)
        string=''.join(string)
    
    return string

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
browser.get("https://www.hackthis.co.uk/levels/coding/2")
    
now = time.time()
    
print ">Sourse code"
page_sourse = BeautifulSoup(browser.page_source, "lxml")
string = str(page_sourse.findAll('textarea')[0].contents[0].decode("utf-8"))

print ">Input: " + str(len(string))
print string
result = sort(string)

print ">Result: " + str(len(string))
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
