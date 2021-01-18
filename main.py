import urllib
from urllib import request
import bs4
from scipy import stats as s
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re



def most_common_words(link):
    '''takes in a link for an article and returns the 10 most common words in the article'''
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
    most_common_list = []
    for a in range(11):
        temp_1 = s.mode(new)[0][0]
        most_common_list.append(temp_1)
        new = [k for k in new if k != temp_1]
    if '' in most_common_list:
        most_common_list.remove('')
    else:
        most_common_list = most_common_list[:len(most_common_list)-1]
    output = []
    for b in most_common_list:
        output.append(b.lower())
    return output



def get_links(link):
    '''takes in a link for a website and returns a list of all the links of articles found on that website '''
    '''specifically designed for google news'''
    req = Request(link)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    articles = []
    for i in links:
        if i != None and i[:10] == './articles':
            correct_link = "news.google.com" + i[1:]
            articles.append(correct_link)
    return articles



def get_most_common_words(link):
    '''takes in a google news link for a specific news category, and outputs a list of the most common words for each of the articles'''
    links = get_links(link)
    output = []
    total_num = len(links)
    for i in range(len(links)):
        output.append(most_common_words(links[i]))
        print ("Currently on link " + i + " out of " + total_num + " links")
    return output