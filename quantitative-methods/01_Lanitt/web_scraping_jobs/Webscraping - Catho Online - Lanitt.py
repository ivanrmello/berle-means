# -*- coding: utf-8 -*-
"""
Created on Thu May 13 00:26:35 2021

@author: ivanr
"""



#Declaring function
def job_info(job):
    
    """ using a soup object from catho online website, extract all necessary
    info from a open position, returning a organized dict
    """
    try:
        job_link  = job.find('a',{"href": True})['href']
    except:
        job_link  = ''
        
    try:
        job_city  = job.find('button',{"class": 'sc-kjoXOD fcitRR'}).get_text(strip=True)
    except:
        job_city  = ''
        
    try:
        job_title  = job.find('h2',{"class": "Title__Heading-sc-14fvmc0-0 fGTSAd sc-csuQGl cBWsYQ"})\
          .get_text(strip=True)
    except:
        job_title  = ''
        
    try:
        job_salary  = job.find('div',{"class": "sc-cJSrbW hqpIYC"}).get_text(strip=True)
    except:
        job_salary  = ''
        
    try:
        job_description  = job.find('span',{"class": "job-description"}).get_text(strip=True)
    except:
        job_description  = ''
        
    try:
        job_description  = job.find('span',{"class": "job-description"}).get_text(strip=True)
    except:
        job_description  = ''
        
    try:
        job_id  = job["data-gtm-dimension-37"]
    except:
        job_id  = ''
        
    try:
        job_date  = job["data-gtm-dimension-44"]
    except:
        job_date  = ''
    
    
    
    return {
        "job_link" : job_link.replace('\n', ' '),
        "job_city" : job_city.replace('\n', ' '),
        "job_title" : job_title.replace('\n', ' '),
        "job_salary" : job_salary.replace('\n', ' '),
        "job_description" : job_description.replace('\n', ' '),
        "job_id" : job_id.replace('\n', ' '),
        "job_date" : job_date.replace('\n', ' ')
        }




import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep


for x in range(222,375):
    print(x)
    url_1 = """
                        https://www.catho.com.br/vagas/?
                        cidade_id%5B0%5D=3195&
                        cidade_id%5B1%5D=3065&
                        cidade_id%5B2%5D=3084&
                        cidade_id%5B3%5D=3053&
                        cidade_id%5B4%5D=3092&
                        cidade_id%5B5%5D=3126&
                        cidade_id%5B6%5D=3252&
                        cidade_id%5B7%5D=3030&
                        cidade_id%5B8%5D=3190&
                        cidade_id%5B9%5D=2998&
                        cidade_id%5B10%5D=3049&
                        cidade_id%5B11%5D=3096&
                        cidade_id%5B12%5D=3093&
                        cidade_id%5B13%5D=3179&
                        cidade_id%5B14%5D=3215&
                        cidade_id%5B15%5D=3149&
                        cidade_id%5B16%5D=3127&
                        cidade_id%5B17%5D=3206&
                        cidade_id%5B18%5D=3001&
                        cidade_id%5B19%5D=3237&
                        cidade_id%5B20%5D=3094&
                        cidade_id%5B21%5D=3107&
                        cidade_id%5B22%5D=3223&
                        cidade_id%5B23%5D=3257&
                        cidade_id%5B24%5D=3138&
                        cidade_id%5B25%5D=3193&
                        cidade_id%5B26%5D=3304
                        """
    url_prefix = "https://www.catho.com.br/vagas/?"
    page = x
    page_final = "page=" + str(page)
    url_sufix = """
                        cidade_id%5B0%5D=3195&
                        cidade_id%5B1%5D=3065&
                        cidade_id%5B2%5D=3084&
                        cidade_id%5B3%5D=3053&
                        cidade_id%5B4%5D=3092&
                        cidade_id%5B5%5D=3126&
                        cidade_id%5B6%5D=3252&
                        cidade_id%5B7%5D=3030&
                        cidade_id%5B8%5D=3190&
                        cidade_id%5B9%5D=2998&
                        cidade_id%5B10%5D=3049&
                        cidade_id%5B11%5D=3096&
                        cidade_id%5B12%5D=3093&
                        cidade_id%5B13%5D=3179&
                        cidade_id%5B14%5D=3215&
                        cidade_id%5B15%5D=3149&
                        cidade_id%5B16%5D=3127&
                        cidade_id%5B17%5D=3206&
                        cidade_id%5B18%5D=3001&
                        cidade_id%5B19%5D=3237&
                        cidade_id%5B20%5D=3094&
                        cidade_id%5B21%5D=3107&
                        cidade_id%5B22%5D=3223&
                        cidade_id%5B23%5D=3257&
                        cidade_id%5B24%5D=3138&
                        cidade_id%5B25%5D=3193&
                        cidade_id%5B26%5D=3304
                """.replace('\n','')
    url_higher_1 = (url_prefix + page_final + url_sufix).replace('\n','')
    
    if x<=1:
        url_to_scrape = url_1
    else:
        url_to_scrape = url_higher_1
    
    html = requests.get(url_to_scrape).text
    soup = BeautifulSoup(html,'html5lib')
    
    jobs_list_page = []
    for job in soup('li',{"data-gtm-dimension-37": True}):
        jobs_list_page.append(job_info(job))
    
    #Creating dframe from list of dicts
    dframe = pd.DataFrame(jobs_list_page)
    
    #Exporting dframe with scraped jobs for this page
    dframe.to_csv(r'C:\Users\ivanr\Documents\86 - Webscraping Jobs\Catho Online\COTEC & EFG\cotec_efg' + str(page) + '.csv', index = False, sep ='|', encoding='utf-8')
    
    #Informing user that we are going to wait
    print("Waiting 30 seconds to scrape next page...")
    
    #Waiting 30 seconds to avoid timeout
    sleep(30)
    
    print("Page " + str(x) + " from 374 scraped successfully")