# Подключение основных модулей
import requests
from bs4 import BeautifulSoup as b


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

            if i == "—" and num >= 1 and li[num+1] == ' 'g:
                li[num] = "\n-"
            elif i == "—":
                li[num] = "-"
            num += 1

        result = ''.join(li)  # AABAAAAAАA

        print(result + "\n")


def main():
    jog = parser(URL)
    printJog2(jog)


if __name__ == "__main__":
    main()



