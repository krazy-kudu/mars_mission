from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    executable_path = {'executable_path' : 'static/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    mars_data = {}

    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)

    time.sleep(10)
    
    news_html = browser.html
    news_soup = bs(news_html, 'html.parser')

    all_article = news_soup.find_all('li', 'slide')
    top_title = all_article[0].find('div', class_='content_title').text
    top_header = all_article[0].find('div', class_='rollover_description_inner').text

    mars_data['top_title'] = top_title
    mars_data['top_header'] = top_header
    
    
 
    # print(mars_data['top_title'])
    # print(mars_data['top_header'])
    
    base_featured_url = 'https://www.jpl.nasa.gov'
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)
    time.sleep(10)

    featured_html = browser.html
    featured_img_soup = bs(featured_html, 'html.parser')
    section = featured_img_soup.find_all('body')
    featured_img = section[0].find_all('img')[5]['src']
    featured_img_url = base_featured_url + featured_img
    
    mars_data['featured_img'] = featured_img_url
    
    
    # print(mars_data['featured_img'])


 
    mars_table_url = 'https://space-facts.com/mars'
    mars_table_dict = {}
    tables = pd.read_html(mars_table_url)
    mars_df = tables[0]
   
    mars_df.columns = ['question', 'answer']

    for value, row in mars_df.iterrows():
        answer = {row['question']: row['answer']}
        mars_table_dict.update(answer)
   
    mars_data['mars_table'] = mars_table_dict

    # print(mars_data['mars_table'])
    
    

    hemisphere_root_url = 'https://astrogeology.usgs.gov'
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    browser.visit(mars_hemispheres_url)
   
    hemispheres_soup = bs(browser.html, 'html.parser')
    
    h3 = hemispheres_soup.find_all('h3')
    title = []
    for x in h3:
        title.append(x.text)
    img_url = []
    
    for link in title:
        
        browser.click_link_by_partial_text(link)
        
        image_soup = bs(browser.html, 'html.parser')
       
        div = image_soup.find_all('div', class_='downloads')
        li = div[0].find_all('li')[0]
        a = li.find_all('a')
        full_size_img = a[0]['href']
        
        img_url.append(full_size_img)
       
        browser.visit(mars_hemispheres_url)
       
        hemisphere_dict = dict(zip(title, img_url))
    
    mars_data['hemispheres'] = hemisphere_dict
    browser.quit()
    
    return mars_data
    print(mars_data)

# mars_data = scrape_info()
# print(mars_data)
