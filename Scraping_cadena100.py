# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 16:29:37 2018

@author: Jordi
"""

from selenium import webdriver
import time
import pandas as pd


def song_cadena100(url, browser):
    browser.get(url)
    info = browser.find_element_by_class_name("track_info").text
    song_info = info.splitlines()
    day_time = time.strftime("%Y/%m/%d - %H:%M:%S")
    if len(song_info) < 2:
        dict = {'tunner': 'cadena100', 'day_time': day_time, 'song': "no info", 'artist': "no info"}
    else:
        dict = {'tunner': 'cadena100', 'day_time': day_time, 'song': song_info[1], 'artist': song_info[0]}
    return dict

url = "http://www.cadena100.es/"
browser = webdriver.Firefox()
browser.get(url) 

data_songs = pd.DataFrame(columns = ['tunner', 'day_time', 'song','artist'])

for i in range(120):
    info_song = song_cadena100(url, browser) 
    if i == 0:
        data_songs = data_songs.append(info_song, ignore_index=True)
    elif info_song.get('song') != data_songs.iloc[-1]['song']:
        data_songs = data_songs.append(info_song, ignore_index=True)
    time.sleep(90)
    
path = "G:/MU Data Science/Tipologia i cicle de vida/PRAC1/"
day = time.strftime("%Y%m%d_%H%M%S")
filename = "dataset_cadena100_" + day + ".xlsx"
data_songs.to_excel(path+filename, encoding="utf-8", index=False)    