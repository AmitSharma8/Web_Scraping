import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# one book scrape
def scrape_book_data(book_url):
    book=requests.get(book_url)
    book_soup=BeautifulSoup(book.content,"html.parser")
    book_data={}
    
    title=book_soup.find(name="h1").get_text()
    book_data["title"]=title
    table_data=book_soup.find_all(name="tr")
    
    for row in table_data:
        key=row.find(name="th").get_text()
        value=row.find(name="td").get_text()
        book_data[key]=value
    book_data["URL"]=book_url
    return book_data

# web page scrape
def scrape_web_page(web_url):
    web_page=requests.get(web_url)
    web_soup=BeautifulSoup(web_page.content,"html.parser")
    books=web_soup.find_all(name="li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    web_page_data=[]
    
    for book in books:
        book_url=book.find(name="a").get("href")
        final_book_url=urljoin(web_url,book_url)
        book_data=scrape_book_data(final_book_url)
        web_page_data.append(book_data)
           
    return web_page_data

def save_to_csv(data, filename):
    headers = data[0].keys() # Get the headers from the first book data dictionary keys
    
    # Open the file and write the data
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        
book_data_list = scrape_web_page("https://books.toscrape.com/index.html")
save_to_csv(book_data_list, "books_data.csv")
print("Data saved to books_data.csv")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    