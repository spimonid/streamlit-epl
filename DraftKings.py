#!/usr/bin/env python
# coding: utf-8

# In[78]:


##FIRST MATCH OF 20-21 EPL (FUL-ARS ON 2020-09-12) IS DK CONTEST NUMBER 39496
##FIRST MATCH OF 16-17 EPL IS DK CONTEST NUMBER 10451


# In[1]:


from selenium import webdriver
import pandas as pd
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from bs4 import BeautifulSoup
import os
import glob
from datetime import datetime
from dateutil.parser import parse
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


# In[2]:


game_days_from_fbref = []


# In[3]:


dk_contest_info = {}


# In[79]:


def dk_contest_check(number):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
#     browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.draftkings.com/draft/lineup/create/' + str(number))
    try:
        time_date = WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]')))
        matchups = browser.find_elements_by_class_name("_2Op1E4hS2OJ8yvwIpEat3M")
        dk_contest_info[number] = [time_date.text, [matchup.text for matchup in matchups]]
        print(number, time_date.text, list(set([matchup.text for matchup in matchups])))
    except:
        pass


# In[77]:


browser = webdriver.Chrome(ChromeDriverManager().install())
x = 39496
while x > 10450:
    dk_contest_check(x)
    x -= 1
    print(x)

