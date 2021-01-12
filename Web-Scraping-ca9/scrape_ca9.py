from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os
import argparse

def web_scrape_page(soup):
    
#     url = driver.current_url

#     resp = requests.get(url)
    
#     # All info from webpage scraped
#     soup = BeautifulSoup(resp.text,'html.parser')
    
    # Scrape coa_dg_table table for all string elements
    data = []
    table = soup.find('table', attrs={'class':'coa_dg_table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
        
    final_df = pd.DataFrame(data)
    final_df = final_df.rename(columns={0: "Case Name", 
                                        1: "Case No.",
                                        2: "Case Panel",
                                        3: "Hearing Location",
                                        4: "Hearing Date",
                                        5: "Audio",
                                        6: "Video"})
    
    # Scrape coa_dg_table table for links to audio and video files
    audio = []
    video = []

    for a in table_body.find_all('a', href=True):
        if 'video' in a['href']:
            video.append(a['href'])
        else:
            audio.append(a['href'])
    
    # Add parent website to beinning of string
    audio = ['https://www.ca9.uscourts.gov/media/' + x for x in audio]
    video = ['https://www.ca9.uscourts.gov/media/' + x for x in video]
    
    # Append to final dataframe
    final_df['Audio'] = audio
    final_df['Video'] = video
    
    
    return final_df

def scrape_coa_dg_table(page_stop):
    #Initializing pg DataFrame that will eventually contain all scraped information
    pg = pd.DataFrame()

    #Using selenium's webdriver to create basic Chrome Options when opening browser
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")

    #Using selenium's webdriver to open Google Chrome with stated options 
    #Goes directly to url which is the first page of IMDB Top 250 list  
    driver = webdriver.Chrome('/anaconda3/envs/capstone/lib/python3.6/site-packages/seleniumbase/drivers/chromedriver', options = options)
    driver.get("https://www.ca9.uscourts.gov/media/")

    #Scrape page until there isn't a 'Next »' button
    #Merge previous pages (pg) to current page (pg_current) until no pages are remaining
    pages_remaining = 0

    while pages_remaining < page_stop+1:
        # Scrape the current page 
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        pg_current = web_scrape_page(soup)
        pg = pd.concat([pg,pg_current])

        # Go to the next page
        next_link = driver.find_element_by_link_text(">>") 
        next_link.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


        print(f"Page {pages_remaining+1} done.")
        pages_remaining += 1

    #Close browser
    driver.close()
    
    # Save table
    pg = pg.reset_index()
    cwd = os.getcwd()
    output_path = cwd + '/ca9.csv'
    pg.to_csv(output_path, index = True)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'page_stop', help='What page to scrape to on ca9.uscourts.gov/media/')
    args = parser.parse_args()

    scrape_coa_dg_table(int(args.page_stop))