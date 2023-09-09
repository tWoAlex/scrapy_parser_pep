# PEP Parser by tWoAlex ⓒ

This spider collects actual info about all **PEP**s (number, title, status) from [peps.python.org](peps.python.org).

---
#### Installation:
```
git clone git@github.com:tWoAlex/scrapy_parser_pep.git
```

---
#### Getting started:

1. Create virtual environment:
```
python -m venv venv   # Windows
```
```
python -m venv env    # Linux
```

2. Install required libraries:
```
source venv/Scripts/activate   # Windows
```
```
source venv/bin/activate       # Linux
```

3. Start script:
```
scrapy crawl pep
```

---
### Results:
By default, results stored in `./results/` directory within two files:

 1. `pep_%creation_date+time%.csv` — table of `Number`, `Title`, `Status`.
 2. `status_summary_%creation_date+time%.csv` — quantity of each `Status`.

Change results folder:
Go to `pep_parse/` ➝ `settings.py` ➝ `RESULTS_DIR`.

---
### About:

#### Based on: **[Scrapy 2.5](https://docs.scrapy.org/en/2.5/)**
#### Author: Александр Муравякин, **[t.me/tWoAlex](https://t.me/tWoAlex)**