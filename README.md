# 📰 News Headlines Web Scraper

## 📌 Objective

This project is a simple web scraper built using Python to extract the latest news headlines from a news website.

---

## 🛠️ Tools & Technologies Used

* Python 🐍
* requests (for sending HTTP requests)
* BeautifulSoup (for parsing HTML)

---

## 🚀 How It Works

* Sends a GET request to the BBC News website
* Retrieves the HTML content of the webpage
* Parses the HTML using BeautifulSoup
* Extracts headlines from `<h1>`, `<h2>`, and `<h3>` tags
* Displays headlines in the terminal
* Saves headlines into a text file

---

## 📂 Project Structure

news-scraper/
│
├── news_scraper.py   # Main Python script
├── headlines.txt     # Output file with headlines
├── README.md         # Project documentation

---

## ▶️ How to Run the Project

### Step 1: Install dependencies

```bash
pip install requests beautifulsoup4
```

### Step 2: Run the script

```bash
python news_scraper.py
```

---

## ✅ Output

* Headlines will be printed in the terminal
* A file named `headlines.txt` will be created containing all headlines

---

## ⚠️ Notes

* Internet connection is required
* Website structure may change, which can affect scraping results
* Headers are used to avoid request blocking

---

## 👤 Author

**Muthumari P**
Python Developer Intern

---

## ⭐ Acknowledgment

This project was created as part of an internship task to demonstrate basic web scraping skills using Python.
