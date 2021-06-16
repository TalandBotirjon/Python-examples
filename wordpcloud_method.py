
"""
* Salom hammaga!
* Pythonni tashqi methodlari juda ko'p. 
* Ulardan requests, bs4, wordcloud va matplotlib methondlardan foydalanamiz.
* Bu methodlarni hammasini kompyuteringizga o'rnatgan bo'lishingiz kerak.
* Yuklab olish uchun cmd ga kirib pip install (requests, bs4, wordcloud, matplotlib) 
* ko'rinishda shu methodlarni o'rnatishimiz kerak.
"""

"""
* Hello everybody!
* There are many external methods of Python.
* We use requests, bs4, wordcloud and matplotlib methondes.
* You must have all of these methods installed on your computer.
* To install, enter cmd and install pip (requests, bs4, wordcloud, matplotlib)
* Apparently we need to install these methods.
"""

"""
* Привет всем!
* Есть много внешних методов Python.
* Мы используем запросы, методы bs4, wordcloud и matplotlib.
* На вашем компьютере должны быть установлены все эти методы.
* Для установки введите cmd и установите pip (запросы, bs4, wordcloud, matplotlib)
* Видимо нам нужно установить эти методы.
"""


import requests      # requests method.  PyPi.org
from bs4 import BeautifulSoup      # BeautifulSoup in bs4 method.   PyPi.org
from wordcloud import WordCloud      # WordCloud  in wordcloud method.   PyPi.org
import matplotlib.pyplot as plt       # plt equal matplotlib.pyplot medoth.   PyPi.org

sahifa = "https://daryo.uz/2021/06/16/ukraina-sputnik-v-bilan-emlanganlarni-kiritmaydi-koronavirusdan-himoyalanishning-noodatiy-usuli-malum-boldi-nyu-yorkda-vaksinatsiya-yutuqlari-salyut-bilan-nishonl/"

def wordphoto(link):    #function Wordphoto  attribute link
        
    links = link
    
    r = requests.get(links)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    news= soup.find( class_="postContent")

    messages = ''
    
    for new in news.text:
        
        messages += new
    
    stopwords = ['uchun', "bo'yicha", 'lekin', 'bilan', 'va', 'bor', 'ham', 'xil', 'yil']
    
    wordcloud = WordCloud(width=1000, height=1000, 
                          background_color='white', stopwords=stopwords,
                          min_font_size=20).generate(messages.upper())
# width and height px.   
    plt.figure(figsize=(8,8),facecolor=None)
    
    plt.imshow(wordcloud)
    
    plt.axis("off")
    
    plt.tight_layout(pad = 0)
    
    plt.show()


wordphoto(sahifa)    

