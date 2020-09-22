from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

mars_data = {}

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path' : 'static/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    table_dict = {}
    mars_table_url = 'https://space-facts.com/mars'
    tables = pd.read_html(mars_url)
    mars_df = tables[0]
    
    mars_df.columns = ['question', 'answer']

    for value, row in mars_df.iterrows():
        answer = {row['question']: row['answer']}
        table_dict.update(answer)
        print(table_dict)
        mars_data['mars_table'] = table_dict
    # # # Visit visitcostarica.herokuapp.com
    # # news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    # # browser.visit(news_url)

    # # time.sleep(3)
    # # all_text = []

    # # # Scrape page into Soup
    # # html = browser.html
    # # soup = bs(html, "html.parser")
    # # title = soup.title.text
    # # print(title)

    # browser = init_browser()
    # hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(hemisphere_url)
    # time.sleep(3)

    # html = browser.html
    # soup = bs(html, 'html.parser')
    # #print(soup.prettify())
                
    # my_xpath = '/html/body/div[1]/div[1]/div[2]/section/div/div[2]'
    # hemi_divs = browser.find_by_xpath(my_xpath)

    # hemi_soup = bs(hemi_divs.html, 'html.parser')

    # print(hemi_soup.prettify)
    # print(len(hemi_soup))
    # link_list = []
    
    # for link in range(len(hemi_soup)):
       
    #     img1_xpath = f'/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[{link+1}]/a'
    #     print(img1_xpath)
        
    #     link_found = browser.links.find_by_partial_href('search/map/Mars')
    #     link_url = link_found
    #     # img_url = browser.find_by_xpath(img1_xpath)
    #     print(link_url)

    #     link = {
    #         'img_url' : link_url
    #     }

    #     link_list.append(link)

    
    # browser.quit()
    # print(link_list)
    # return link_list
    # #print(soup.prettify())
    
    # # for thing in soup:
    # #     # article_title = soup.find('div', class_='content_title').find('a').text
    # #     # article_head = soup.find('div', class_='rollover_description_inner').text

    # #     article_title = browser.find_by_tag('div', class_='content_title').find_by_tag('a').text
    # #     article_head = browser.find_by_tag('div', class_='rollover_description_inner').text
    # #     # title_text = browser.find_by_tag(title_soup).text 
    # #     # head_text = browser.find_by_tag(head_soup).text
        
    # #     article_text = {
    # #         # 'title' : article_title,
    # #         # 'head' : article_head
    # #         'title' : title_text,
    # #         'head' : head_text
    # #         }
    
    # #     all_text.append(article_text)
    
    # # print(all_text)
    # # return all_text
    
   
    # browser = init_browser()

    # base_url = 'https://www.jpl.nasa.gov'
    # featured_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(featured_img_url)
    # time.sleep(3)

    # site_html = browser.html
    # img_soup = bs(site_html, 'html.parser')
    # featured_img = img_soup.find('img', class_='carousel_item')['src']
    # featured_img_url = bas_url + featured_img

    # print(featured_img_url)

    
    # return featured_img_url


print(mars_data)