# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

def scrape_info():

    # Import BeautifulSoup
    from bs4 import BeautifulSoup



    import pandas as pd
    import time



    # Import Splinter and set the chromedriver path
    from splinter import Browser
    executable_path = {"executable_path": "C:/Users/brent/USC-LA-DATA-PT-08-2019-U-C/12-Web-Scraping-and-Document-Databases/Homework/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)



    # Visit the following URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(4)

    # scrape page into Soup, will be able to call multiple times
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Scrape Title and paragrah
    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    # print(news_title)
    # print(news_p)


    # Set URL
    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    time.sleep(4)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Full-sized feature image Mars
    image = soup.find('a', {'class': ['button fancybox']}).text
    # image = image.find("img")["data-fancybox-href"]
    # image_url = "https://www.jpl.nasa.gov" + image

    # print(image)

    #set url
    url="https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(20)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Get today's weather in Mars
    weather = soup.find('div', {'class': 'css-901oao'}).text
        
    # print(weather)


    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    #set url
    url="https://space-facts.com/mars/"
    browser.visit(url)
    time.sleep(4)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Get Mars facts
    facts = soup.find('table', {'class': ['tablepress-id-p-mars']})
    marsp_df_facts = pd.read_html(str(facts))[0] # Panda soup
    marsp_df_facts = marsp_df_facts.to_html() # Python to HTML



    # Set URL
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(4)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    marscollect = [] # empty list

    # Full-sized feature image Mars
    marscollect = soup.find_all('div', class_='item')
    temp = []
    for i in marscollect:
        temp.append("https://astrogeology.usgs.gov" + i.a['href'])  
    print(temp)


    urlcollections = []
    for i in temp:
        response = requests.get(i) 
        soup = BeautifulSoup(response.text, 'html.parser')
        urlimage = soup.find('div', class_="downloads").a['href']
        titletext = soup.find("h2", class_="title").text
        urlcollections.append({"title":titletext, "img_url":urlimage})
    print(urlcollections)

    marsdata = {"title":news_title, "text":news_p, "img_url":urlimage, "marspanda":marsp_df_facts, "marscollect":urlcollections, "marsweather":weather, "marsimage":image}

    return marsdata



