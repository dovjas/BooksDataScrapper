<h1>Books Data Scraper</h1>

This is a python web scraping script to get the newest books data from knygos.lt.

Modules:
- BeautifulSoup;
- Request;
- CSV;

1. Use Requests to fetch URL;
2. Create BeautifulSoup object and parse HTML content;
3. Find the elements containing data attributes: 
  a) Author
  b) Title
  c) New price,
  d) Old price,
  e) Stock;
5. Loop over(pagination);
6. Create csv file and fill with data.

