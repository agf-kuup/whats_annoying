from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from itertools import cycle
import os
import time # Just to wait a bit between messages.


driver_path='chrome_driver/chromedriver.exe'
name_victim="Vale Chay"
looping=False

def infinitize_text(loop):
    '''Generates a cycle or a list of messages 
    depending on the variable looping.'''

    if not loop:
        messages=[l for l in open('content.txt','r+')]
    else:
        messages=cycle([l for l in open('content.txt','r+')])
    return messages

def search_chat(driv,victim):
    '''
    Looks for the search box in the chat window.
    '''
    path_to_search='//*[@id="side"]/div[1]/div/label/div/div[2]'
    searcher=driv.find_element_by_xpath(path_to_search)
    searcher.send_keys(victim)
    time.sleep(1) # Gives time the browser updates the search of the victim
    pray_found='//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div'
    pray=driv.find_element_by_xpath(pray_found)
    pray.click()

def send_msg(mbox,msgs,loop):
    '''
    Writes the next message in the input box and sends it.
    '''    
    if loop:
        mbox.send_keys(next(msgs))
    else:
        mbox.send_keys(msgs.pop(0))
    
    time.sleep(1)
    mbox.send_keys(Keys.ENTER)

def start_annoying(driv,loop):
    path_message_box='//*[@id="main"]/footer/div[1]/div[2]'
    messages=infinitize_text(loop)

    i=len(messages) if type(messages)==list else -1
    
    messageBox=driv.find_element_by_xpath(path_message_box)
    messageBox.click()
        
    while i:    
        send_msg(messageBox,messages,loop)
        i-=1

def start(_victim,_driver,_loop):
    driver = webdriver.Chrome(executable_path=r'{}'.format(_driver))
    driver.get("https://web.whatsapp.com/")
    input("Click when QR is done")
    time.sleep(5)
    search_chat(driver,_victim)
    start_annoying(driver,_loop)
    driver.close()


start(name_victim,driver_path,looping)