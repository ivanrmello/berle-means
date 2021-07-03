# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:37:06 2021

@author: ivanr
"""

import pandas as pd
import glob

path = r'C:\Users\ivanr\Documents\86 - Webscraping Jobs\Catho Online\COTEC & EFG' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, sep='|')
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv(r'C:\Users\ivanr\Documents\86 - Webscraping Jobs\Catho Online\COTEC & EFG\cotec_efg_catho_online_all_jobs.csv', index = False, sep ='|', encoding='utf-8')