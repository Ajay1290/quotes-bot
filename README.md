# qoutes-bot

Simple Scrapy "quotes bot" to scrape quotes along with there authors and relavent tags assigned to them from the internet.

it stores all the data in SQL table using SQLite database.

it does all the cleaning, processing and checks on data before adding them into the database.

## How To Use


1. pull the repo for the source code.

```shell
  path/to/dir> git pull https://github.com/Ajay1290/quotes-bot
```

2. install the dependecies from [req.txt](./req.txt) using pip.

```shell
  path/to/quotes-bot> pip install -r req.txt
```

3. start the service (make sure wi-fi is connected)

```shell
  path/to/quotes-bot> scrapy crawl quote
```

this will start the service and create a quotes.db in the root of your folder.

### More on Files

- [quote.py](./quotes/spiders/quote.py) is the file where you should look at.
- [patls.json](./patl.json) contains folder structure of this project 
  - [Patl](https://github.com/Ajay1290/Patl) is another open-source project of mine do check it out! &#128512;
- [quotes-sample.json](./quotes-sample.json) contains sample processed data extracted from the internet
- quotes.db will be created when you run the service

### Links

- Code: <https://github.com/Ajay1290/quotes-bot>
- Issue tracker: <https://github.com/Ajay1290/quotes-bot/issues>
