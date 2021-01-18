'''
from main import most_common_words
link = "https://www.theatlantic.com/ideas/archive/2020/11/trump-proved-authoritarians-can-get-elected-america/617023/"
print (most_common_words(link))
'''



from main import get_links
temp = get_links("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pRU3lnQVAB?hl=en-PK&gl=PK&ceid=PK%3Aen")
print (temp)



'''
from main import get_most_common_words
print (get_most_common_words("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pRU3lnQVAB?hl=en-PK&gl=PK&ceid=PK%3Aen"))
'''