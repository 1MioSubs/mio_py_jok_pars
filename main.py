# Подключение основных модулей
import requests
from bs4 import BeautifulSoup as b
import sqlite3 as sq


with sq.connect("jok.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS joktext (
    text TEXT NOT NULL,
    send INTEGER NOT NULL DEFAULT 0
    )""")


# Заполнение переменных ссылки и масива анегдотов
URL = 'https://www.anekdot.ru/release/anekdot/year'
list_of_jokes = ["В Израиле, в отличие от других стран, дружно живут евреи разных национальностей.", "Если хочешь попасть в телевизор - не нужно далеко от него отходить, а то можешь не добросить."]


# Парсер сайта по ссылке выше
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


def printJog(jog):
    test = 0
    for i in jog:
        test += 1
        x = i.replace('- ', '\n- ') #—
        x2 = x.replace('— ', '\n- ') #—
        print(x2 + "\n")
    print(test)


def printJog2(jog):

    for s in jog:
        li = list(s)
        num = 0
        for i in li:

            if i == "-" and num >= 1 and li[num+1] == ' ':
                li[num] = "\n-"

            if i == "—" and num >= 1 and li[num+1] == ' ':
                li[num] = "\n-"
            elif i == "—":
                li[num] = "-"
            num += 1

        result = ''.join(li)

        with sq.connect("jok.db") as con2:
            cur2 = con2.cursor()
            cur2.execute(f"INSERT INTO joktext (text) VALUES ('{str(result)}')")

        print(result + "\n")


def main():
    jog = parser(URL)
    printJog2(jog)


if __name__ == "__main__":
    main()



