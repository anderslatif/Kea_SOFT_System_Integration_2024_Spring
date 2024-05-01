
<div class="title-card" style="color: cyan;">
    <h1>Web Scraping</h1>
</div>

---

# Web Scraping vs. Web Crawling?

- **Web <u>scraping</u>**: downloading structured data from the web.

- **Web <u>crawling</u>**: downloading the web pages.

---

# Web Scraping vs Web Crawling

Note that the legal documents enforce rules on data mining and not web scraping. Difference:

- **Web scraping**: extracting the data.

- **Data mining**: analyzing the data (often involving extensive data sets).


---

# Rules and legality

1. Do not break websites. 

2. You can scrape public data. But if the data isn't intended to be public, you can't scrape it.

3. The Danish law [Ophavsretslovens § 11b](https://www.elov.dk/ophavsretsloven/paragraf/11b/) is based on the EU directive [DSM-direktivets artikel 4.](https://eur-lex.europa.eu/eli/dir/2019/790/oj) 

4. Do not violate Copyright laws.

5. Do not violate the GDPR.


---

# Anti-scraping Techniques

Example: [https://www.ikea.com/dk/da/](https://www.ikea.com/dk/da/)
[Pricerunnner - Disallow rules](https://www.pricerunner.dk/robots.txt)

<img src="./assets/anti-scraping_techniques.png" alt="anti-scraping techniques">

Source: https://kinsta.com/knowledgebase/what-is-web-scraping/


---

# Politeness

https://en.wikipedia.org/wiki/Spider_trap#Politeness

Rules for politeness:

1. **Crawl-delay**: Create a delay between requests.

2. **Respect User-agent rules**: The name of the bot.

3. **Respect Allow/Disallow rules**: The pages that should not be crawled.

4. **Respect Sitemap rules**: The sitemap of the website.

---

# Web Scraping Tools

Example of categories:

<img src=".//assets/web_scraping_tools.png" alt="web-scraping tools" style="height: 40vh;">

---

<div class="title-card" style="color: cyan;">
    <h1>Hands-on: Node (Cheerio), BeautifulSoup4 and Scrapy</h1>
</div>

