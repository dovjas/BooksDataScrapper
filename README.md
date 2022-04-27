<h1>Books Data Scraper</h1>

This is a python web scraping script to get books data from knygos.lt,
using BeautifulSoup for pulling data out of HTML.
I used it to scrape around 700k Arabic reviews in 2018 (Arabic reviews are fewer than English ones).


Modules:
BeautifulSoup,
Request,
CSV,

1. Use requests to fetch URL;
2. Create soup object and parse HTML content;
3. Find the elements containing data attributes: Author,Title,Newprice,Old price,Stock;
4. Loop over(pagination);
5. Create csv file and fill with data.

This scraper was built during a class assignment for JOUR4001: Foundations of Computing, Fall 2021.
