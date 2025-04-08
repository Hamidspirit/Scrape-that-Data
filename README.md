# Scrape-That-Data

After making a web-scraper in GO i wanted to see if python was better choice.
python has better tooles for scraping and i'am using [scrapy](https://scrapy.org/) in this project.

to make a scraper and use it well i need to know how to work with *CSS selector* and
*XPath* .

with developer tools i can get the css selector for HTML elements that i want.

this is good document [MDN-CSS-Selector](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)

this one helps to get the idea how selector supposed to work in scraping [Selector-for-Scraping](https://www.scrapingbee.com/blog/using-css-selectors-for-web-scraping/)

i will be using MongoDB and pymongo for storing data.

scrapy has a built in testing system using docstrings valled contracts.
i use that but i also can use pytest or unittest.

some common issues for scraping data still persist in here too,
like how to extract dynamically generated data, retrying failed requests,
getting around websites with anti-scraping mechanism.

scrapy provides some middleware for retrying failed request.
Python was better exprience for scraping than Go, python abstracts many things.

scraper in [GO](https://github.com/Hamidspirit/web-scraper)