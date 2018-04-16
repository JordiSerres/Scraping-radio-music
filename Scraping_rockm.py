# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 18:41:15 2018
Scraping rockfm
@author: Jordi
"""

from selenium import webdriver
import time
import pandas as pd

def song_rockfm(url, browser):
    browser.get(url)
    info = browser.find_element_by_xpath("//div[contains(@id, 'metadata_player')]").text
    song_info = info.splitlines()
    day_time = time.strftime("%Y/%m/%d - %H:%M:%S")
    if len(song_info) != 2:
        dict = {'tunner': 'rockfm', 'day_time': day_time, 'song': "no info", 'artist': "no info"}
    else:
        dict = {'tunner': 'rockfm', 'day_time': day_time, 'song': song_info[1], 'artist': song_info[0]}
    return dict


url = "http://player.rockfm.fm/"
browser = webdriver.Firefox()
browser.get(url) 

data_rockfm_songs = pd.DataFrame(columns = ['tunner', 'day_time', 'song','artist'])

for i in range(120):
    info_song = song_rockfm(url, browser) 
    if i == 0:
        data_rockfm_songs = data_rockfm_songs.append(info_song, ignore_index=True)
    elif info_song.get('song') != data_rockfm_songs.iloc[-1]['song']:
        data_rockfm_songs = data_rockfm_songs.append(info_song, ignore_index=True)
    time.sleep(90)
    
path = "G:/MU Data Science/Tipologia i cicle de vida/PRAC1/"
day = time.strftime("%Y%m%d_%H%M%S")
filename = "dataset_rockfm_" + day + ".xlsx"
data_rockfm_songs.to_excel(path+filename, encoding="utf-8", index=False)