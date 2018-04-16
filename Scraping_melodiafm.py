# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:50:46 2018
Scraping melodia fm
@author: Jordi
"""

from selenium import webdriver
import time
import pandas as pd

def song_melodiafm(url, browser):
    browser.get(url)
    info = browser.find_element_by_class_name("info").text
    song_list_info = info.splitlines()
    song_list_info = song_list_info[1:]
    day_time = time.strftime("%Y/%m/%d - %H:%M:%S")
    return song_list_info, day_time

url = "http://www.melodia-fm.com/directo/"
browser = webdriver.Firefox()
browser.get(url) 
data_melodiafm_songs = pd.DataFrame(columns = ['tunner', 'day_time', 'song','artist'])
separator = " - "
for i in range(36):
    print i
    list_melodiafm, day_time = song_melodiafm(url, browser)
    if len(list_melodiafm) > 1:
        if data_melodiafm_songs.shape[0] == 0:
            for song in list_melodiafm:
                track = song.split(separator)
                info_song = {'tunner': 'melodiafm', 'day_time': day_time, 'song': track[1], 'artist': track[0]}
                data_melodiafm_songs = data_melodiafm_songs.append(info_song, ignore_index=True)        
        elif data_melodiafm_songs.iloc[-1]['song'] == list_melodiafm[-1].split(separator)[1]:
            print u"és la mateixa llista"
        else:
            for song in list_melodiafm:
                track = song.split(separator)
                info_song = {'tunner': 'melodiafm', 'day_time': day_time, 'song': track[1], 'artist': track[0]}
                data_melodiafm_songs = data_melodiafm_songs.append(info_song, ignore_index=True)
    else:
        info_song = {'tunner': 'melodiafm', 'day_time': day_time, 'song': "no info", 'artist': "no info"}
        data_melodiafm_songs = data_melodiafm_songs.append(info_song, ignore_index=True)                        
    time.sleep(600)

path = "G:/MU Data Science/Tipologia i cicle de vida/PRAC1/"
day = time.strftime("%Y%m%d_%H%M%S")
filename = "dataset_melodiafm_" + day + ".xlsx"
data_melodiafm_songs.to_excel(path+filename, encoding="utf-8", index=False)

   