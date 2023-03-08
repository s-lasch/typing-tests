import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import os

# enter username
username = ""

# enter password
password = ""

global file
file = "C:/Users/steve/Downloads/results.csv"

def get_data():
    # open a Chrome driver
    browser = webdriver.Chrome()

    # go to the login page
    browser.get('https://monkeytype.com/login')
	
	# accept all cookies
    browser.find_element_by_xpath('//*[@id="cookiePopup"]/div[2]/div[2]/div[1]').click()
	
    time.sleep(1.5)

    # enter username
    assert username != ""
    browser.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/input[1]').send_keys(username)

    # enter password
    assert password != ""
    browser.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/input[2]').send_keys(password)

    # click sign-in button
    browser.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/div[2]').click()

    try:
        # wait for the page to load
        time.sleep(3)
        
        # remove file if it already exists
        try:
            os.remove(file)
        except Exception:
            pass

        # download CSV data
        browser.find_element_by_xpath('//*[@id="middle"]/div[6]/div[3]/div[11]/div').click()

        # wait for download to complete
        time.sleep(4)
		
    except Exception as e:
        # raise any exceptions
        raise e

    # close the browser
    browser.close()


def switch_delimiter(filename, delimiter_to, delimiter_from):
    # convert the pipe delimited csv to a comma delimited csv
    with open(file, "r") as file_pipe:

        # save the new file 
        with open(filename, 'w') as file_comma:
            csv.writer(file_comma, delimiter=delimiter_to).writerows(csv.reader(file_pipe, delimiter=delimiter_from))

