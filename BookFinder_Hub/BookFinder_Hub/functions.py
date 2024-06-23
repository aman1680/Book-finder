import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrmOpts = Options()
# chrmOpts.add_argument('--headless=new')
# chrmOpts.add_argument('--log-level=1')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}
    
def flipkart_scrap(book="", author="", publisher=""):
    toFind = book+author+publisher
    driver = webdriver.Chrome(options=chrmOpts)
    URL = 'https://www.flipkart.com/'
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Input book name to find
    xpath = '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input'
    field = driver.find_element(by=By.XPATH, value=xpath)
    field.send_keys(toFind)
    field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    
    # Find and analyse results after search 
    className = 'slAVV4'
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
    eleList = driver.find_elements(by=By.CLASS_NAME, value=className)
    # Eliminating sponsored links
    n = 0
    for i, ele in enumerate(eleList):
        tmp = (ele.find_element(by=By.CLASS_NAME, value='a-row')).find_element(by=By.CLASS_NAME, value='a-color-secondary')
        if tmp.text != 'Sponsored':
            n = i
            break

    products = []
    nos = 5 if len(eleList)-n>=5 else min(len(eleList), n)
    try:
        for i in range(nos):
            eleInterest = eleList[n+i]
            # products = {'site': 'flipkart', 'name': [], 'price':[], 'desc':[], 'link': []}
            prod = {}
            prod['site'] = 'flipkart'
            prod['image'] = eleInterest.find_element(by=By.TAG_NAME, value='img').get_attribute('src')
            prod['name'] = eleInterest.find_element(by=By.CLASS_NAME, value='wjcEIp').text
            prod['price'] = eleInterest.find_element(by=By.CLASS_NAME, value='Nx9bqj').text
            prod['desc'] = eleInterest.find_element(by=By.CLASS_NAME, value='NqpwHC').text
            prod['link'] = eleInterest.find_element(by=By.CLASS_NAME, value='wjcEIp').get_attribute('href')
            products.append(prod)
    except:
        print('error in flipkart')
        products = None
    
    driver.quit()
    return products


def amazon_scrap(book="", author="", publisher=""):
    toFind = book+author+publisher
    driver = webdriver.Chrome(options=chrmOpts)
    URL = 'https://www.amazon.in/'
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Input book name to find
    xpath = '//*[@id="twotabsearchtextbox"]'
    field = driver.find_element(by=By.XPATH, value=xpath)
    field.send_keys(toFind)
    field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Find and analyse results after search 
    className = 'puis-card-container'
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
    eleList = driver.find_elements(by=By.CLASS_NAME, value=className)
    # Eliminating sponsored links
    n = 0
    for i, ele in enumerate(eleList):
        tmp = (ele.find_element(by=By.CLASS_NAME, value='a-row')).find_element(by=By.CLASS_NAME, value='a-color-secondary')
        if tmp.text != 'Sponsored':
            n = i
            break
    # Extracting required data
    products = []
    nos = 5 if len(eleList)-n>=5 else min(len(eleList), n)
    try:
        for i in range(nos):
            eleInterest = eleList[n+i]
            prod = {}
            prod['site'] = 'amazon'
            prod['image'] = eleInterest.find_element(by=By.TAG_NAME, value='img').get_attribute('src')
            prod['name'] = (eleInterest.find_element(by=By.TAG_NAME, value='h2')).find_element(by=By.CLASS_NAME, value='a-size-medium').text
            prod['price'] = 'Rs.'+(eleInterest.find_element(by=By.CLASS_NAME, value='a-price')).find_element(by=By.CLASS_NAME, value='a-price-whole').text
            prod['desc'] = ''
            prod['link'] = (eleInterest.find_element(by=By.CLASS_NAME, value='puisg-col-inner')).find_element(by=By.TAG_NAME, value='a').get_attribute('href')
            products.append(prod)
    except:
        print('error in amazon')
        products = None

    driver.quit()    
    return products


def crossword_scrap(book="", author="", publisher=""):
    toFind = book+author+publisher
    driver = webdriver.Chrome(options=chrmOpts)
    URL = 'https://www.crossword.in/'
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Input book name to find
    xpath = '//*[@id="shopify-section-header"]/div/div[1]/div[1]/div/div[2]/div/div/form/input[3]'
    field = driver.find_element(by=By.XPATH, value=xpath)
    field.send_keys(toFind)
    field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Find and analyse results after search 
    className = 'wizzy-result-product-item'
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
    eleList = driver.find_elements(by=By.CLASS_NAME, value=className)
    # Eliminating sponsored links
    n = 0
    products = []
    nos = 5 if len(eleList)-n>=5 else min(len(eleList), n)
    try:
        for i in range(nos):
            eleInterest = eleList[n+i]
            prod = {}
            prod['site'] = 'crossword'
            prod['image'] = (eleInterest.find_element(by=By.TAG_NAME, value='img')).get_attribute('src')
            prod['name'] = eleInterest.find_element(by=By.CLASS_NAME, value='product-item-title').text
            prod['price'] = eleInterest.find_element(by=By.CLASS_NAME, value='wizzy-product-item-price').text
            prod['desc'] = eleInterest.find_element(by=By.CLASS_NAME, value='product-item-author').text
            prod['link'] = eleInterest.get_attribute('href')
            products.append(prod)
    except:
        print('error in crossword')
        products = None
    
    driver.quit()    
    return products



def snapdeal_scrap(book="", author="", publisher=""):
    toFind = book+author+publisher
    driver = webdriver.Chrome(options=chrmOpts)
    URL = 'https://www.snapdeal.com/'
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Input book name to find
    xpath = '//*[@id="inputValEnter"]'
    field = driver.find_element(by=By.XPATH, value=xpath)
    field.send_keys(toFind)
    field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Find and analyse results after search 
    className = 'product-tuple-listing'
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
    eleList = driver.find_elements(by=By.CLASS_NAME, value=className)
    # Eliminating sponsored links
    n = 0
    # Extracting required data
    products = []
    nos = 5 if len(eleList)-n>=5 else min(len(eleList), n)
    try:
        for i in range(nos):
            eleInterest = eleList[n+i]
            prod = {}
            prod['site'] = 'snapdeal'
            prod['image'] = (eleInterest.find_element(by=By.TAG_NAME, value='img')).get_attribute('src')
            prod['name'] = eleInterest.find_element(by=By.CLASS_NAME, value='product-title').text
            prod['price'] = (eleInterest.find_element(by=By.CLASS_NAME, value='product-price-row')).find_element(by=By.CLASS_NAME, value='product-price').text
            prod['desc'] = ''
            prod['link'] = eleInterest.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
            products.append(prod)
    except:
        print('error in snapdeal')
        products = None

    driver.quit()
    return products


def bookscape_scrap(book="", author="", publisher=""):
    toFind = book+author+publisher
    #driver = webdriver.Chrome(options=chrmOpts)
    driver = webdriver.Chrome()
    URL = 'https://www.bookscape.com/'
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Input book name to find
    xpath = '//*[@id="__next"]/div[1]/nav/div[3]/div[2]/div[2]/form/input'
    field = driver.find_element(by=By.XPATH, value=xpath)
    field.send_keys(toFind)
    field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Find and analyse results after search 
    xpath = '//*[@id="__next"]/div[2]/div[2]/div/div/div[1]/div/section/div/div[4]/div[2]/div/section/div[1]/div[1]'
#   xpath = '//*[@id="__next"]/div[2]/div[2]/div/div/div[1]/div/section/div/div[4]/div[2]/div/section/div[2]/div[1]/article'
#//*[@id="__next"]/div[2]/div[2]/div/div/div[1]/div/section/div/div[4]/div[2]/div/section/div[2]/div[1]/article
#
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    # Extracting required data
    products = []
    try:
        for i in range(5):
            xpath = f'//*[@id="__next"]/div[2]/div[2]/div/div/div[1]/div/section/div/div[4]/div[2]/div/section/div[1]/div[{i+1}]'
            eleInterest = driver.find_element(by=By.XPATH, value=xpath)
            prod = {}
            prod['site'] = 'bookscape'
            prod['image'] = (eleInterest.find_elements(by=By.TAG_NAME, value='img'))[3].get_attribute('src')
            prod['name'] = eleInterest.find_element(by=By.CLASS_NAME, value='book_title_label').text
            prod['price'] = (eleInterest.find_element(by=By.CLASS_NAME, value='offer_price')).find_element(by=By.TAG_NAME, value='span').text
            prod['desc'] = (eleInterest.find_element(by=By.CLASS_NAME, value='book_desc_label')).find_element(by=By.TAG_NAME, value='span').text
            prod['link'] = eleInterest.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
            products.append(prod)
    except:
        print('error in boospace')
        products = None

    driver.quit()
    return products


def theindianbookstrore_scrap(book:str = "", author:str = "", publisher:str = ""):
    print(type(book))
    print(type(author))
    print(type(publisher))
    toFind = book+author+publisher
    driver = webdriver.Chrome(options=chrmOpts)
    URL = 'https://www.theindianbookstore.in/'
    driver.get(URL)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    # Input book name to find
    driver.find_element(by=By.CLASS_NAME, value='icon-search').click()
    xpath = '//*[@id="Search-In-Modal"]'
    field = driver.find_element(by=By.XPATH, value=xpath)
    field.send_keys(toFind)
    field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    # Find and analyse results after search 
    className = 'card-wrapper'
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
    eleList = driver.find_elements(by=By.CLASS_NAME, value=className)
    # Eliminating sponsored links
    n = 0
    # for i, ele in enumerate(eleList):
    #     tmp = (ele.find_element(by=By.CLASS_NAME, value='a-row')).find_element(by=By.CLASS_NAME, value='a-color-secondary')
    #     if tmp.text != 'Sponsored':
    #         n = i
    #         break
    # Extracting required data
    products = []
    nos = 5 if len(eleList)-n>=5 else min(len(eleList), n)
    try:
        for i in range(nos):
            eleInterest = eleList[n+i]
            prod = {}
            prod['site'] = 'theindianbookstore'
            prod['image'] = (eleInterest.find_element(by=By.TAG_NAME, value='img')).get_attribute('src')
            prod['name'] = eleInterest.find_element(by=By.TAG_NAME, value='a').get_attribute('innerHTML')
            prod['price'] = (eleInterest.find_element(by=By.CLASS_NAME, value='price__container')).find_elements(by=By.TAG_NAME, value='span')[5].text
            prod['desc'] = ''
            prod['link'] = eleInterest.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
            products.append(prod)
    except:
        print('error in theindianbookstore')
        products = None

    driver.quit()
    return products


def scrap_websites(book = "", author = "", publisher = ""):
    results = []
    
    try:
        flipkart = flipkart_scrap(book, author, publisher)
        results.append(flipkart)
        print("Successfully scraped data from flipkart!!")
    
        amazon = amazon_scrap(book, author, publisher)
        results.append(amazon)
        print("Successfully scraped data from amazon!!")

        # crossword = crossword_scrap(book, author, publisher)
        # results.append(crossword)
        # print("Successfully scraped data from crossword!!")


        # bookscape = bookscape_scrap(book, author, publisher)
        # results.append(bookscape) 
        # print("Successfully scraped data from bookscape!!")

        theindianbookstrore = theindianbookstrore_scrap(book, author, publisher)
        results.append(theindianbookstrore)
        print("Successfully scraped data from theindianbookstore!!")

    except Exception as e:
        print(e)
    
    return results
