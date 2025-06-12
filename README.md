## ‣ Investors Crawler PoC

This repository contains a proof-of-concept scraper for extracting data from web directories. It currently targets dance studios in Helsinki using [Finder.fi](https://www.finder.fi).

---

## ‣ Prerequisites

- Python 3.7+
- Git
- Windows PowerShell (if on Windows)

---

## ‣ Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd investors-crawler 
   ```
2. Create and activate a virtual environment:
    ```bash
   python -m venv venv
    . venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
    ```bash
   pip install -r requirements.txt
   ```

---

## ‣ Usage
1. Navigate to the scripts folder:
   ```bash
   cd scripts
   ```
2. Run the scraper:
    ```bash
   python scraper_finder.py
   ```
3. Check the output CSV in data/finder_studios_helsinki.csv.

--- 
## ‣ Debugging
If you need to inspect the HTML fetched by the scraper, a debug_finder.html file will be generated in scripts/. Open it in your browser to update selectors.

--- 
## ‣ Authors
* Alba Marmolejo Ramos - [AlbaMarm](https://github.com/AlbaMarm)