import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class AudibleScraper:
    def __init__(self, headless: bool = True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)

    def scrape(self, url: str, max_pages: int = None) -> pd.DataFrame:
        self.driver.get(url)

        # find total pages
        pagination = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, './/ul[contains(@class,"pagingElements")]'))
        )
        pages = pagination.find_elements(By.TAG_NAME, "li")
        last_page = int(pages[-2].text)

        if max_pages:
            last_page = min(last_page, max_pages)

        current_page = 1
        titles, authors, durations = [], [], []

        while current_page <= last_page:
            print(f"Scraping page {current_page}/{last_page}...")

            # wait for book container
            container = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "adbl-impression-container"))
            )
            products = container.find_elements(By.XPATH, './/li[contains(@class,"productListItem")]')

            for product in products:
                try:
                    title = product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text
                except:
                    title = "N/A"

                try:
                    author = product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text
                except:
                    author = "N/A"

                try:
                    duration = product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text
                except:
                    duration = "N/A"

                titles.append(title)
                authors.append(author)
                durations.append(duration)

            current_page += 1
            try:
                next_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[contains(@class,"nextButton")]'))
                )
                next_button.click()
            except:
                print("No more pages found.")
                break

        self.driver.quit()
        return pd.DataFrame({"title": titles, "author": authors, "length": durations})


if __name__ == "__main__":
    scraper = AudibleScraper(headless=True)
    df = scraper.scrape("https://www.audible.com/search", max_pages=3)
    df.to_csv("books.csv", index=False)
    print("✅ Scraping complete. Data saved to books.csv")
