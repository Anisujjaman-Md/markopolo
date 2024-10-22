import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models, schemas

def scrape_watches():
    url = "https://www.amazon.com/s?k=watches"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    for item in soup.select(".s-main-slot .s-result-item"):
        brand = item.select_one(".s-brand-name").text
        model = item.select_one(".s-title").text
        price = float(item.select_one(".s-price").text.replace("$", ""))
        specifications = "Specifications here"
        image_url = item.select_one("img")["src"]


        db = SessionLocal()
        db_product = models.Product(brand=brand, model=model, price=price, specifications=specifications, image_url=image_url)
        db.add(db_product)
        db.commit()
        db.close()

if __name__ == "__main__":
    scrape_watches()
