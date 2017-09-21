import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from PyDictionary import PyDictionary
from nltk.stem import PorterStemmer
import goslate
import translate
from langdetect import detect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.

browser.get("https://www.mygov.in/group-issue/share-your-ideas-pm-narendra-modis-mann-ki-baat-26th-march-2017/")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")
ptr = browser.find_element_by_css_selector('.pager-next.first.last')
#no_of_pagedowns = 10

i = 0

while(i<250):
    time.sleep(12)
    ptr = browser.find_element_by_css_selector('.pager-next.first.last')
    ptr.click()
    """link = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "View More")))
    ActionChains(browser).move_to_element(link).perform()
    link.click()"""

    i = i + 1

no_of_pagedowns = 150
time.sleep(10)
while (no_of_pagedowns > 0):
        elem.send_keys(Keys.PAGE_DOWN)
        # ptr.click()
        time.sleep(0.2)

        no_of_pagedowns = no_of_pagedowns - 1;

time.sleep(1)

paras=[]
post_elems = browser.find_elements_by_class_name("comment_body")

count=0;
#stop_words = set(stopwords.words('english'))
for post in post_elems:
    file = open('C:\\Users\\Simran\\PycharmProjects\\AI\\pos.txt',"a")
    print(post.text)
    str1 = post.text
    """language_id = detect(str1)
    if(language_id=='hi'):
            for word in str1.split():
                print(word)
                dictionary = PyDictionary(word)
                word = dictionary.translateTo("en")"""


    str1 = str1.encode('ascii', 'ignore')
    file.write(str1.decode('ascii'))

    #paras = post.text
    count= count+1;
print(count)
file.close()
""""word_tokens = word_tokenize(sent_tokenize(post.text),language="english")
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(ps.stem(w))
            #dictionary = PyDictionary(w)

            #file = open("test.txt", "w")
            #list = dictionary.translateTo("es")
            #str1 = ''.join(str(e) for e in list)
            #print(str1)

    #print(word_tokens)
    print(filtered_sentence)"""