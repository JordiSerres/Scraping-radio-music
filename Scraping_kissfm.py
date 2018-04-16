# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:58:43 2018
Scraping kissfm
@author: Jordi
"""

from selenium import webdriver
import time
import pandas as pd

def song_kissfm(url, browser):
    browser.get(url)
    artist = browser.find_element_by_class_name("autor").text
    song =  browser.find_element_by_class_name("titulo").text                                              
    day_time = time.strftime("%Y/%m/%d - %H:%M:%S")
    song_list_info = {'tunner': 'kissfm', 'day_time': day_time, 'song': song, 'artist': artist}
    return song_list_info

url = "http://kissfm.es/player/"
browser = webdriver.Firefox()
browser.get(url) 

data_kissfm_songs = pd.DataFrame(columns = ['tunner', 'day_time', 'song','artist'])

for i in range(120):
    info_song = song_kissfm(url, browser) 
    if i == 0:
        data_kissfm_songs = data_kissfm_songs.append(info_song, ignore_index=True)
    elif info_song.get('song') != data_kissfm_songs.iloc[-1]['song']:
        data_kissfm_songs = data_kissfm_songs.append(info_song, ignore_index=True)
    time.sleep(90)
    
path = "G:/MU Data Science/Tipologia i cicle de vida/PRAC1/"
day = time.strftime("%Y%m%d_%H%M%S")
filename = "dataset_kissfm_" + day + ".xlsx"
data_kissfm_songs.to_excel(path+filename, encoding="utf-8", index=False)    

