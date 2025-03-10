# Scrapy Quotes Scraper

This project is a Scrapy-based web scraper that extracts quotes, authors, and tags from [Quotes to Scrape](http://quotes.toscrape.com/) and stores the data in JSON, CSV, and XML formats.

## Features
- Scrapes quotes, authors, and tags from the website.
- Saves the extracted data into **JSON, CSV, and XML** files.
- Uses Scrapy framework for structured web scraping.

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/RaeesFatima/Web-scrapping
cd Scrapy
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate     # For Windows

For pycharm users its not necessary to create virtual enviroment manaually, 
it creates on its own when project is created.
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### 1. Run the Scraper
```bash
scrapy crawl quotes -o quotes.json
scrapy crawl quotes -o quotes.csv
scrapy crawl quotes -o quotes.xml
```
This will create `quotes.json`, `quotes.csv`, and `quotes.xml` files in the project directory.

### 2. Project Structure
```
.
Scrapy/
│── .venv/                      
│── firstscrapy/
│   │── firstscrapy/
│   │   │── spiders/
│   │   │   │── __init__.py
│   │   │   │── quotes_spider.py
│   │   │── __init__.py
│   │   │── items.py
│   │   │── middlewares.py
│   │   │── pipelines.py
│   │   │── settings.py
│── output/
│   │── quotes.csv
│   │── quotes.json
│   │── quotes.xml
│── scrapy.cfg
│── README.md
│── External Libraries/
│── Scratches and Consoles/


```

## Example Output
### JSON Format (`quotes.json`)
```json
[
  {
    "text": "The only limit to our realization of tomorrow is our doubts of today.",
    "author": "Franklin D. Roosevelt",
    "tags": ["motivational", "future"]
  }
]
```

## Project Purpose
This project is created for learning purposes to practice web scraping using Scrapy. It helps in understanding how to extract data from websites and store it in different formats.

## Conclusion
This Scrapy project provides a simple yet effective way to extract quotes, authors, and tags from the Quotes to Scrape website. It demonstrates how to use Scrapy for web scraping and store data in different formats. You can expand this project by adding more features like scraping multiple pages, handling JavaScript-rendered content, or integrating with a database for storage.

