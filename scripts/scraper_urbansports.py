import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ──────────────────────────────────────────────────────────────────────────────
# Configuración
# ──────────────────────────────────────────────────────────────────────────────
CITY      = "aachen"
BASE_URL  = f"https://urbansportsclub.com/de/venues/{CITY}"
MAX_ITEMS = 60
# ──────────────────────────────────────────────────────────────────────────────

def scrape_urbansports():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=opts)

    driver.get(BASE_URL)
    time.sleep(5)

    # scroll hasta el final para cargar todo
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    elems = driver.find_elements(By.XPATH, "//a[starts-with(@href, '/de/venues/')]")
    data, seen = [], set()
    for e in elems:
        href = e.get_attribute("href")
        if not href or href.endswith("/de/venues") or href in seen:
            continue
        seen.add(href)

        # intenta extraer el <h3> interno, si no coge todo el texto
        try:
            name = e.find_element(By.TAG_NAME, "h3").text.strip()
        except:
            name = e.text.strip()

        data.append({"name": name, "url": href})
        if len(data) >= MAX_ITEMS:
            break

    driver.quit()
    return data

def save_csv(rows):
    os.makedirs("../data", exist_ok=True)
    # usa CITY para nombrar el CSV
    filename = f"urbansports_venues_{CITY}.csv"
    path = os.path.join("..", "data", filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "url"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ {len(rows)} venues guardados en {path}")

if __name__ == "__main__":
    venues = scrape_urbansports()
    # imprime los primeros 5 para que veas ya algo por consola
    for v in venues[:5]:
        print("·", v)
    save_csv(venues)
