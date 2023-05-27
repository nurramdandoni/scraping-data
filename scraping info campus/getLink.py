'''
Google Map Scraper Using Selenium
Code By Sunil
17 July, 2022
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import csv
import time
from bs4 import BeautifulSoup

search = ".ac.id"
pages = 7

header = ["data_cid", "title", "address", "website", "phone", "rating","image","category","timing","description","profiles"]
data = []

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.headless = True
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com')

driver.implicitly_wait(2)
driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)
more = driver.find_element(By.TAG_NAME,"g-more-link")
more_btn = more.find_element(By.TAG_NAME,"a")
more_btn.click()
time.sleep(10)

for page in range(1, pages+1):
    elements = driver.find_elements(By.CSS_SELECTOR, 'div#search a[class="vwVdIc wzN8Ac rllt__link a-no-hover-decoration"')
    counter = 1
    for element in elements:
        data_cid = element.get_attribute('data-cid')
        element.click()
        print('item click... 5 seconds...')
        time.sleep(5)

        #title
        title = driver.find_element(By.CSS_SELECTOR,'h2[data-attrid="title"]')

        print('title: ', title.text)
        #address
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/location/location:address"] span:nth-child(2)')
            if len(temp_obj.text) > 0:
                address = temp_obj.text
        except NoSuchElementException:
            address =""
        print ('address: ',address)
        #website
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/local:unified_actions"]')
            innerHTML = temp_obj.get_attribute('innerHTML')

            # Parse the innerHTML using BeautifulSoup
            soup = BeautifulSoup(innerHTML, 'html.parser')

            # Get the href value
            if soup.a:
                href = soup.a['href']
            else:
                href = None
            if temp_obj.text == 'Website':
                website = href
            else:
                website = href
        except NoSuchElementException:
            website = href

        print('website:', website)

        #phone
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/collection/knowledge_panels/has_phone:phone"] span:nth-child(2) > span > a > span')
            if len(temp_obj.text) > 0:
                phone = temp_obj.text
        except NoSuchElementException:
            phone =""

        print('phone:', phone)
        #rating
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'g-review-stars span')
            if len(temp_obj.get_attribute('aria-label')) > 0:
                rating = temp_obj.get_attribute('aria-label')
        except NoSuchElementException:
            rating =""

        print('rating:',rating)
        #total review
        # try:
        #     temp_obj = driver.find_element(By.CSS_SELECTOR, 'a[data-async-trigger="reviewDialog"] span')
        #     if len(temp_obj.text) > 0:
        #         reviews = temp_obj.text
        # except NoSuchElementException:
        #     reviews =""
        # print('reviews:', reviews)

        #image
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/location/location:media"] > div > a > div')
            
            if len(temp_obj.get_attribute('style')) > 0:
                image = temp_obj.get_attribute('style')
                if 'background' in image:
                    image = image.replace('background-image: url("','')
                    image = image.replace('"','')
                    image = image.replace(');','')
        except NoSuchElementException:
            image =""
        print('image:', image)

        #category
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/local:lu attribute list"] > div > div > span')
            if len(temp_obj.text) > 0:
                category = temp_obj.text
        except NoSuchElementException:
            try:
                temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/local:one line summary"] > div > span')
                if len(temp_obj.text) > 0:
                    category = temp_obj.text
            except NoSuchElementException:
                category=""
        print('category:', category)

        #timing
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/location/location:hours"] > div > div > div:nth-child(2) > div > table')
            if len(temp_obj.get_attribute('innerHTML')) > 0:
                timing = temp_obj.get_attribute('innerHTML')
                timing = "<table>"+timing.replace(' class="SKNSIb"','')+"</table>"
        except NoSuchElementException:
            timing =""
        print('timing:', timing)

        #description
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-long-text]')
            if len(temp_obj.get_attribute('data-long-text')) > 0:
                description = temp_obj.get_attribute('data-long-text')
        except NoSuchElementException:
            '''
            try:
                temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/local:merchant_description"] > c-wiz > div > div:nth-child(2)')
                if len(temp_obj.get_attribute('innerHTML')) > 0:
                    description = temp_obj.get_attribute('innerHTML')
            except NoSuchElementException:
                description =""
            '''
            description=""
            
        # print('description:', description) // this is for testing
        # social profiles
        profiles=""
        for s_count in range (1, 6):
            try:
                temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/common/topic:social media presence"] div:nth-child(2) > div:nth-child(' + str(s_count) + ') > div > g-link > a')
                if len(temp_obj.get_attribute('href')) > 0:
                    profiles_str = temp_obj.get_attribute('href')
            except NoSuchElementException:
                profiles_str = ""
                break
            profiles += "<br/>" + profiles_str
        print('profiles: ', profiles)




        #print(counter, data_cid, title.text, address, website, phone,rating,reviews,image,category,timing,description,profiles)
        row = [data_cid, title.text, address, website, phone,rating,image,category,timing,description,profiles]
        data.append(row)
        counter+=1
    try:
        page += 1
        page_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Page ' + str(page) + '"]')
        innerHTML = temp_obj.get_attribute('innerHTML')
        print('innerHTML:', innerHTML)
        page_button.click()
        print('page click... 10 seconds...')
        time.sleep(10)
    except NoSuchElementException:
        break

with open('gmap.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)