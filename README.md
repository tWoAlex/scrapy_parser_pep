# PEP Parser by tWoAlex ⓒ

### Powered by **Srapy ([scrapy.org](https://scrapy.org/))**

This spider collects actual info about all **PEP**s (number, title, status) from [peps.python.org](peps.python.org).

#### Installation:

```
git clone git@github.com:tWoAlex/scrapy_parser_pep.git
```

#### Getting started:
<details>
<summary>Manual</summary>

>1. Create virtual environment:
>```
>python -m venv venv   # Windows
>```
>or
>```
>python -m venv env    # Linux
>```
>2. Install required libraries:
>```
>source venv/Scripts/activate   # Windows
>```
>or
>```
>source venv/bin/activate       # Linux
>```
>3. Start script:
>```
>scrapy crawl pep
>```
>
</details>

### Results:
Results stored in `./results/` directory. You may change it in `pep_parse/settings.py/RESULTS_DIR`.