import json
from bs4 import BeautifulSoup 

def seperate(orders):
    order_numbers = []
    for order in orders:
        order_numbers.append(order["OrderNumber"])

    result = open("seperate_result.txt","w+")
    result.write(f"{tuple(order_numbers)}")

def extract_data(html):
    content = open('scrapetest.html','r')
    soup = BeautifulSoup(content.read(), 'html.parser')
    data = []

    for td in soup.find_all('td', class_="dataCell"):
        anchor = soup.find_all('a')
        for a in anchor:
            if '0036' in a.contents[0]:
                data.append(a.contents[0])
    return data

def regex(json):
    nos = []
    for no in json["items"]:
        nos.append(no["INVFICHENO"])

    result = open("regex_result.txt","w+")
    result.write(f"{tuple(nos)}")

    return tuple(nos)

def regex2(json):
    nos = []
    for no in json["items"]:
        nos.append(no["ORFFICHENO"])

    result = open("regex_result2.txt","w+")
    result.write(f"{tuple(nos)}")

    return tuple(nos)

def add_comma(txt):
    numbers = []
    for number in txt:
        numbers.append('00'+number[:-1])

    result = open("without_comma_result.txt", "w+")
    result.write(f"{tuple(numbers)}")

    return tuple(numbers)

def add_comma2(txt):
    numbers = {}
    i=0
    for number in txt:
        if number[:-1] not in numbers.values():
            numbers[i] = number[:-1]
        i+=1

    result = open("add_coma2.txt", "w+")
    result.write(f"{tuple(numbers.values())}")

    return numbers

if __name__ == '__main__':
    orders = json.load(open('orders.json'))
    seperate(orders)

    invoices = json.load(open('invoices.json'))


    numbers = open("without_comma.txt", "r")

    add_comma(numbers)