import requests
from bs4 import BeautifulSoup

# News website URL
url = "https://www.bbc.com/news"

# Add headers (important to avoid blocking)
headers = {"User-Agent": "Mozilla/5.0"}

# Send GET request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all headlines
headlines = soup.find_all(["h1", "h2", "h3"])

# Save to file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines):
        text = headline.get_text(strip=True)

        if text:
            print(f"{i+1}. {text}")
            file.write(f"{i+1}. {text}\n")

print("✅ Headlines saved successfully!")