import sqlite3 as sq
from telebot import TeleBot
from time import sleep


bot = TeleBot('6172751642:AAHsqozZiTiamTKILZ5vpZHU3ajn8hUQOGI')

def seldb():
    with sq.connect("jok.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT rowid, text, send FROM joktext WHERE send = '0'")
        test = cur.fetchmany(12)
    return test


def updatedb(rowjok):
    with sq.connect("jok.db") as con:
        cur = con.cursor()
        cur.execute(f"UPDATE joktext SET send = '1' WHERE rowid = '{int(rowjok)}'")


def sendjok(joklists):
    for joklist in joklists:

        li = list(joklist[1])
        num = 0
        for i in li:

            if i == "-" and num >= 1 and li[num + 1] == ' ':
                li[num] = "\n-"

            if i == "—" and num >= 1 and li[num + 1] == ' ':
                li[num] = "\n-"
            elif i == "—":
                li[num] = "-"
            num += 1

        result = ''.join(li)
        bot.send_message(-1001846761780, result + "\n\n@smekhovichok")
        print(result + "\n\n@smekhovichok" + "\n\n")
        updatedb(joklist[0])
        sleep(7200)


def main():
    numsend = 0
    while True:
        if numsend == 1:
            break
        joklists = seldb()
        sendjok(joklists)
        print("\n")
        numsend += 1


if __name__ == "__main__":
    main()
