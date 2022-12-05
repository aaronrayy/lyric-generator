from bs4 import BeautifulSoup
import requests

def scrape(link, out):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')
    content = soup.find(id="content")  
    f = open(out, 'w')    
    for element in content:
        if str(element) != "<br/>":
            f.write(str(element))
    f.close()

# url = requests.get("https://www.lyricsfreak.com/e/eminem/lose+yourself_20049853.html")
# soup = BeautifulSoup(url.content, 'html.parser')
# content = soup.find(id="content")  
# f = open("scraper.txt", 'w')  
# print(content)  
# for element in content:
#     if str(element) != "<br/>":
#         f.write(str(element))
# f.close()

# website tutorial for beautiful soup i used:
# https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/ 