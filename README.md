# Audible Scraper

A simple Python project that scrapes audiobook data (title, author, duration) from **Audible** using Selenium and saves the results into a CSV file.

⚠️ **Disclaimer**: This project is for **educational purposes only**. Audible’s Terms of Service prohibit automated scraping for commercial use. Please use responsibly.

---

## ✨ Features

* Scrapes multiple pages of search results
* Extracts **title, author, and length** of each audiobook
* Saves results into a clean `books.csv` file
* Supports **headless mode** (runs without opening a browser window)
* Handles pagination automatically

---

## 📂 Project Structure

```
AudibleScraper/
│── audible_scraper.py   # main scraper script  
│── requirements.txt     # dependencies  
│── README.md            # project overview  
│── .gitignore           # ignored files (venv, cache, CSV, etc.)  
```

---

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/mahmoudsalamaa9/AudibleScraper
cd AudibleScraper
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the scraper**

```bash
python audible_scraper.py
```

This will generate a `books.csv` file with the scraped data.
