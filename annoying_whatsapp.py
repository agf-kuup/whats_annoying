from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from itertools import cycle
import os
import time # Just to wait a bit between messages.


@dataclass
class annoy:
    victim: str                         # Name of the chat you will look for.
    size: int=None                      # Number of messages you want to send.
    loop: bool=False                    # The content will be repeated forever.
    if loop:
        messages=cycle([l for l in open('content.txt','r+')])
    else:
        messages=[l for l in open('content.txt','r+')]

    @staticmethod
    def search_chat(driv,victim):
        path_to_search='//*[@id="side"]/div[1]/div/label/div/div[2]'
        searcher=driv.find_element_by_xpath(path_to_search)
        searcher.send_keys(victim)
        time.sleep(1) # Gives time the browser updates the search of the victim
        pray_found='//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div'
        pray=driv.find_element_by_xpath(pray_found)
        pray.click()

    @staticmethod
    def send_msg(mbox):
        if annoy.loop:
            mbox.send_keys(Keys.ENTER)
            time.sleep(1)
            mbox.send_keys(next(annoy.messages))
            time.sleep(1)
            mbox.send_keys(Keys.ENTER)
        else:
            mbox.send_keys(Keys.ENTER)
            time.sleep(1)
            mbox.send_keys(self.messages.pop(0))
            time.sleep(1)
            mbox.send_keys(Keys.ENTER)

    @staticmethod
    def start_annoying(driv,msgs,size):
        i=size if size else -1 
        
        messageBox=driv.find_element_by_class_name("_1Plpp")
        messageBox.click()

        while i:    
            self.send_msg(messageBox)
            i-=1

    @property
    def run(self):
        driver = webdriver.Chrome(executable_path=r'chrome_driver/chromedriver.exe')
        driver.get("https://web.whatsapp.com/")
        input("Click when QR is done")
        time.sleep(5)
        self.search_chat(driver,self.victim)
        self.start_annoying(driver,self.messages,self.size)
        driver.close()

A=annoy(victim="Vale Chay")
A.run
