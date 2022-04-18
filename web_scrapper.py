import requests
from bs4 import BeautifulSoup

def get_news():
    news = {}

    url = "https://www.cariverplate.com.ar/noticias-de-entradas"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    eq = soup.findAll("a", class_="titulo")

    for x in eq:
        news_url = "https://www.cariverplate.com.ar/" + x["href"]
        page = requests.get(news_url)
        soup2 = BeautifulSoup(page.content, "html.parser")

        eq2 = soup2.find("figcaption")
        eq3 = eq2.findAll("p")
        full_text = ""
        for y in eq3:
            full_text = full_text + y.text + "\n"

        news[x.text] = full_text

    return news