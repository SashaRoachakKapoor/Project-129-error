import bs4 as BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
import requests

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

scraped_data=[]
emptystr=['star_name','radius','mass','distance_data']

def scrape(hyperlink):
    page=requests.get(hyperlink)
    page=page.find_all('table')
    for tr_tag in soup.find_all('tr', attrs={'class': 'fact_row'}):
        td_tags=tr_tag.find_all('td')
        for td_tag in td_tags:
                try:
                    templist.append(td_tag.find_all('div',attrs={'class':'value'})[0].contents[0])
                except:
                    templist.append('')
    soup=BeautifulSoup(browser.page_source,'html.parser')
    bright_star_table=soup.find('table',attrs={'class','wikitable'})
    table_body=bright_star_table.find('tbody')
    table_rows=table_body.find_all('tr')

    for row in table_rows:
        table_cols=row.find_all('td')
        #print(table_cols)
        templist=[]

        for col_data in table_cols:
            #print(col_data.text)
            data=col_data.text.strip()
            #print(data)
            templist.append(data)
            scraped_data.append(templist)

stars_data=[]
for i in range(0,len(scraped_data)):
    Star_names=scraped_data[i][1]
    Distance=scraped_data[i][3]
    Mass=scraped_data[i][5]
    Radius=scraped_data[i][6]
    Lum=scraped_data[i][7]

    required_data=[Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

stars_df_1 = pd.read_csv("updated_scraped_data.csv")

for index, row in stars_df_1.iterrows():
    scraped_data('hyperlink')

    print(f"Data Scraping at hyperlink {index+1} completed")

headers=['Star_names','Distance','Mass','Radius','Lum']
star_df_1=pd.DataFrame(stars_data,columns=headers)
star_df_1.to_csv("scraped_data.csv",index=True,index_label='id')

#stars_df_1.head()
stars_df_1.dropna(rows=['NaN'],inplace=True)

mass_column=float('mass_column')*0.000954588
radius_column=float('radius_column')*0.102763


