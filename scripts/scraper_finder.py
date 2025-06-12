import requests, csv, os
from bs4 import BeautifulSoup

URL = "https://www.finder.fi/search?what=tanssikoulu+Helsinki"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def scrape_finder():
    resp = requests.get(URL, headers=HEADERS, timeout=15)
    with open("debug_finder.html", "w", encoding="utf-8") as f:
        f.write(resp.text)
    print("🔍 debug_finder.html")

    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    titles = soup.select("h2.MuiTypography-h3")
    data = []
    for h2 in titles:
        name = h2.get_text(strip=True)

        link_tag = h2.find_parent("a")
        profile = None
        if link_tag and link_tag.has_attr("href"):
            profile = link_tag["href"]
            if profile.startswith("/"):
                profile = "https://www.finder.fi" + profile

        data.append({"name": name, "profile": profile})

    return data

def save_csv(rows):
    os.makedirs("../data", exist_ok=True)
    path = "../data/finder_studios_helsinki.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name","profile"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ {len(rows)} studios saved in {path}")

if __name__ == "__main__":
    estudios = scrape_finder()
    save_csv(estudios)
