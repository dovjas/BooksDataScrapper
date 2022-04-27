<h1>Books Data Scraper</h1>

This is a python web scraping script to get the newest books data from knygos.lt.

Modules:
- BeautifulSoup;
- Request;
- CSV;

1. Use Requests to fetch URL;
2. Create BeautifulSoup object and parse HTML content;
3. Find the elements containing data attributes: 
 - Author
 - Title
 - New price,
 - Old price,
 - Stock;
5. Loop over(pagination);
6. Create csv file and fill with data.

This scraper was built during a class assignment for JOUR4001: Foundations of Computing, Fall 2021.
