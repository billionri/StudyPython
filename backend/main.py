from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import requests
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Python Challenge API running 🚀"}

@app.get("/random")
def random_challenge():
    url = "https://www.geeksforgeeks.org/python-programming-examples/"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.select("a[href*='/python-program']")
    if not links:
        return {"error": "Failed to fetch problems"}

    item = random.choice(links)
    title = item.text.strip()
    href = item["href"]
    description = f"Try solving: {title} — full problem at {href}"
    return {
        "title": title,
        "description": description,
        "hint": "Use loops, conditions, or built-ins depending on problem type.",
        "sampleInput": "Your sample input here",
        "sampleOutput": "Expected output here"
    }
