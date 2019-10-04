from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.ansa.it/sito/notizie/topnews/index.shtml")

tot_art = []
articles = driver.find_elements_by_class_name("news")
for article in articles:
    tot_art.append(article.find_element_by_class_name('news-title').text )

driver.close()

with open('result_ansa.txt', 'w') as F:
    F.write("\n".join(tot_art))
