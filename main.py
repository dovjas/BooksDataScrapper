from bs4 import BeautifulSoup
import requests
from csv import writer

with open("knygos.csv", "w", encoding="utf8", newline='') as file:
    thewriter = writer(file)
    header = ['Author', 'Title', 'New price', 'Old price', 'Stock']
    thewriter.writerow(header)

    for page in range(1, 14):
        url = "https://www.knygos.lt/lt/knygos/naujos/?psl=" + str(page)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        books = soup.find_all("div", {"class": "product"})
        for book in books:
            try:
                author = book.find("span", {"class": "book-properties book-author"}).text.strip()
            except:
                author = 'No data'
            try:
                title = book.find("span", {"class": "book-properties book-title"}).text
            except:
                title = 'No data'
            try:
                new_price = book.find("span", {"class": "book-properties book-price new-price"}).text
            except:
                new_price = 'No data'
            try:
                old_price = book.find("span", {"class": "book-properties book-price old-price"}).text
            except:
                old_price = 'No data'
            try:
                stock = book.find("p", {"class": "availability"}).text
            except:
                stock = 'No data'

            book_data = [author, title, new_price, old_price, stock]

            thewriter.writerow(book_data)