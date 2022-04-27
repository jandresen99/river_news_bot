import requests
from bs4 import BeautifulSoup

def get_newsV2():
    news = {}

    url = "https://www.cariverplate.com.ar/noticias-de-entradas"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    eq = soup.findAll("a", class_="titulo")

    for x in eq:
        news_url = "https://www.cariverplate.com.ar/" + x["href"]
        page = requests.get(news_url)
        soup2 = BeautifulSoup(page.content, "html.parser")

        title = "**" + x.text + "**"

        eq2 = soup2.find("figcaption")
        eq3 = eq2.findAll("p")
        full_text = ""
        for y in eq3:
            eq4 = y.findAll("strong")

            bolds_processed = []

            for string in eq4:
                text = string.text
                new_string = text.replace("<strong>", "")
                new_string = new_string.replace("</strong>", "")

                bolds_processed.append(new_string)

            new_text = y.text

            if new_text in bolds_processed:
                new_text = "**" + new_text + "**"

            full_text = full_text + new_text + "\n"
            print(y)
            print(full_text)
            print("\n")
            print("\n")
            break

        news[title] = full_text

    return news


def get_newsV1():
    news = {}

    url = "https://www.cariverplate.com.ar/noticias-de-entradas"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    eq = soup.findAll("a", class_="titulo")

    for x in eq:
        news_url = "https://www.cariverplate.com.ar/" + x["href"]

        title = u'🚨' + x.text

        news[title] = news_url

    return news
