import requests
from bs4 import BeautifulSoup
import sys


while True:
    user_question = input("Enter type of currency. USD or EURO: ").upper()
    if user_question == "EXIT":
        print("See you again!")
        sys.exit()
    else:
        def main_function_currency(url):
            soup = BeautifulSoup(requests.get(url).text, features="lxml")
            info_of_currency = soup.find('div', {'class': 'au-mid-buysell'}).text
            return print_result(info_of_currency.split(sep="\n", maxsplit=4)[2].split(sep=" ")[0])

        def print_result(res):
            print("Курс {} на чорному ринку на даний час = {} грн.".format(user_question,res))

        def exchange_information_online(curr_type):
            if curr_type == "USD":
                url ="https://minfin.com.ua/ua/currency/auction/usd/sell/lvov/?presort=&sort=time&order=desc"
                return main_function_currency(url)

            elif curr_type == "EURO":
                url_euro ="https://minfin.com.ua/ua/currency/auction/eur/sell/lvov/?presort=&sort=time&order=desc"
                return main_function_currency(url_euro)
            else:
                print("Something information is not good")
                print("You enter this symbol of currency: {} ".format(user_question))
                return

        exchange_information_online(user_question)
