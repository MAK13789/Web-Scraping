'''
MAKE STUFF INTO FUNCTIONS FIRST
'''
import urllib
from urllib import request
import bs4
from statistics import mode
link = "https://www.theatlantic.com/ideas/archive/2020/11/trump-proved-authoritarians-can-get-elected-america/617023/"
f = urllib.request.urlopen(link)
soup = bs4.BeautifulSoup(f)
for script in soup(["script", "style"]):
    script.decompose()
strips = list(soup.stripped_strings)
adjusted = strips[60:len(strips)-10]
temp = ''
for i in range(len(adjusted)):
    temp += adjusted[i]
    temp += ' '
j = len(temp) - 1
while j >= 0:
    if temp[j].isalpha() == False and temp[j] != ' ' and temp[j] != "'":
        temp = temp[:j] + temp[j+1:]
    j -= 1
new = list(temp.split(' '))
from scipy import stats as s
most_common_list = []
for a in range(11):
    temp_1 = s.mode(new)[0][0]
    most_common_list.append(temp_1)
    new = [k for k in new if k != temp_1]
if '' in most_common_list:
    most_common_list.remove('')
else:
    most_common_list = most_common_list[:len(most_common_list)-1]
print (most_common_list)
'''
#finding the links of all the websites on google news (for a specific "type":
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox('C:\\Users\\Ahsan\\Downloads\\geckodriver.exe')
driver.get("https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFZ4ZERBU0FtVnVLQUFQAQ?hl=en-CA&gl=CA&ceid=CA:en")
elems = driver.find_element_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
'''




#USE TRY EXCEPT OR STH fOR WHEN THE MODE ISNT UNIQUE
#MAKE THESE STUFF INTO FUNCTIONS SO THAT IT IS EASIER WHEN MULTIPLE ARTICLES ARE USED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#find a better way to split this so that it always starst from the beginning of the text and ends at the end of the text 
#(for example, finding where the title or date is)
#for now, just split it at some arbritrary indices that should work for most articles
#delete all non-letters (SPACES SHOuLD STAY THO)
#maybe remove capitals
#write it so that it scrapes google news or sth
#so the type of the article would be given, and it would determine the most used words for that article
#append that into a database
#in the end you can see if there's a relation between most used words and type of article, and if so, use ML