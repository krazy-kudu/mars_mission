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
    
    
 
    print(mars_data)

    
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
    
    
    print(mars_data)


 
    mars_table_url = 'https://space-facts.com/mars'
    mars_table_dict = {}
    tables = pd.read_html(mars_table_url)
    mars_df = tables[0]
   
    mars_df.columns = ['question', 'answer']

    for value, row in mars_df.iterrows():
        answer = {row['question']: row['answer']}
        mars_table_dict.update(answer)
   
    mars_data['mars_table'] = mars_table_dict


    
    print(mars_data)

    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    browser.visit(mars_hemispheres_url)
   
    hemispheres_soup = bs(browser.html, 'html.parser')
    #print(hemispheres_soup.prettify())
    
    
    h3 = hemispheres_soup.find_all('h3')
    title = []
    for title in h3:
        title.append(title.text)
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
        
        hemisphere_image_urls = dict(zip(title, img_url))
   
        mars_data['hemispheres'] = hemisphere_image_urls

    
    print(mars_data)
    # hemisphere_base_url = 'https://astrogeology.usgs.gov'
    # page_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    # browser.visit(page_url)
   
    # hemisphere_soup = bs(browser.html, 'html.parser')
  
    # heading = hemisphere_soup.find_all('h3')
    # title = []
    # for title in heading:
    #     title.append(title.text)

    # hemi_img_urls = []
    
    # for href in title:
        
    #     browser.click_link_by_partial_text(href)
    #     hemi_soup = bs(browser.html, 'html.parser')
        
    #     div = hemi_soup.find_all('div', class_='itemLink product-item')
    #     li = div[0].find_all('li')[0]
    #     a = li.find_all('a')
    #     full_img_url = a[0]['href']
      
    #     hemi_img_urls.append(full_img_url)
    #     #Return back to main page
    #     browser.visit(page_url)
    #     #Zip titles and img_url into dictionary.
    #     hemisphere_img_urls = dict(zip(title, img_url)) 
    #     mars_data['hemispheres' : hemisphere_img_urls]
    # print(mars_data)

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

   
    browser.quit()
    print(mars_data)
    return mars_data
    
mars_data = scrape_info()
print(mars_data)