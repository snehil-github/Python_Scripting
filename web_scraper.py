import requests
import re
import mymailapi
from bs4 import BeautifulSoup

def web_scraper(URL, comp_price : int = None):

    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}
    # headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    pattern = r'\d'
    reg_price = re.findall(pattern, price, flags=0)
    str_price = [str(i) for i in reg_price[:-3]]
    res_price = int("".join(str_price))

    if res_price <= comp_price:
        print("Your Wishlist Product is:\n",title.strip())
        mymailapi.email_sender()
    else:
        print(r"Sorry! Price is still high: %d\-" %res_price)



"""
This is a main function which takes user input and call web_scraper() function.

"""

if __name__ == "__main__":

    URL = "https://www.amazon.in/Apple-Watch-GPS-Cellular-40mm/dp/B07XWZ681Q/ref=sr_1_1?crid=1PASPEACYWJK9&dchild=1&keywords=apple+iwatch&qid=1620500785&sprefix=apple+iwa%2Caps%2C302&sr=8-1"
    # URL = input("Please enter product url: ")
    comp_price = int(input("Enter price you want to check: ")) 
    web_scraper(URL, comp_price)