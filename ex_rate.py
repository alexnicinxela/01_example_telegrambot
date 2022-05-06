import requests
from bs4 import BeautifulSoup
def get_rate():
    url = "https://cbr.ru/"
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.855 Yowser/2.5 Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text

    """with open("index.html", "w", encoding="utf-16") as file:
        file.write(src)
    
    with open("index.html", "r") as file:
        src = file.read()"""

    soup = BeautifulSoup(src, "lxml")
    ex_rate = soup.find_all(class_="col-md-2 col-xs-9 _right mono-num")
    rates = [elem.text.strip() for elem in ex_rate]

    #print(f'Доллар:\nПокупка {rates[0]}\nПродажа {rates[1]}')
    mess = f'Доллар\nПокупка: {rates[0]}\nПродажа: {rates[1]}\n\nЕвро\nПокупка: {rates[2]}\nПродажа: {rates[3]}'
    return mess