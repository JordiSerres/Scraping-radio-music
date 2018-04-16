# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:09:27 2018

@author: Jordi
"""

from selenium import webdriver
import time
import pandas as pd

def song_europafm(url, browser):
    browser.get(url)
    info = browser.find_element_by_class_name("listado").text
    song_list_info = info.splitlines()
    song_list_info = song_list_info[1:]
    day_time = time.strftime("%Y/%m/%d - %H:%M:%S")
    return song_list_info, day_time

url = "http://www.europafm.com/directo/"
browser = webdriver.Firefox()
browser.get(url) 

data_europafm_songs = pd.DataFrame(columns = ['tunner', 'day_time', 'song','artist'])
separator = "- "
for i in range(36):
    list_europafm, day_time = song_europafm(url, browser)
    if data_europafm_songs.shape[0] == 0:     
        for song in list_europafm:
            track = song.split(separator)
            info_song = {'tunner': 'europafm', 'day_time': day_time, 'song': track[1], 'artist': track[0]}
            data_europafm_songs = data_europafm_songs.append(info_song, ignore_index=True)
    elif data_europafm_songs.iloc[-1]['song'] == list_europafm[-1].split(separator)[1]:
        print u"és la mateixa llista"
    else:
        for song in list_europafm:
            track = song.split(separator)
            info_song = {'tunner': 'europafm', 'day_time': day_time, 'song': track[1], 'artist': track[0]}
            data_europafm_songs = data_europafm_songs.append(info_song, ignore_index=True)
    time.sleep(300)
    
path = "G:/MU Data Science/Tipologia i cicle de vida/PRAC1/"
day = time.strftime("%Y%m%d_%H%M%S")
filename = "dataset_europafm_" + day + ".xlsx"
data_europafm_songs.to_excel(path+filename, encoding="utf-8")    
    