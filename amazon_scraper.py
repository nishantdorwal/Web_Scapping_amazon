"""
scraper.py
-----------
Scrapes book details from a saved Amazon HTML file (amazon.html)
and saves the results to an Excel file(amazon_books.xlsx) or csv (amazon_books.csv).

This method is used because direct requests to Amazon often return
HTTP Error 503 (Service Unavailable).
"""

from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_html(file_path="amazon.html", output_file="amazon_books.xlsx"):
    # --- Step 1: Read the saved HTML file ---
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: {file_path} not found. Please save the Amazon page first.")
        return

    # --- Step 2: Parse with BeautifulSoup ---
    soup = BeautifulSoup(html_content, "lxml")

    # --- Step 3: Find all book containers ---
    books = soup.find_all("div", class_="zg-grid-general-faceout")

    data = []

    # --- Step 4: Extract details ---
    for book in books:
        try:
            book_name = book.find("div", class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").get_text(strip=True)
        except:
            book_name = " "

        try:
            author = book.find("div", class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").get_text(strip=True)
        except:
            author = " "

        try:
            rating = book.find("span", class_="a-icon-alt").get_text(strip=True)
        except:
            rating = " "

        try:
            reviews = book.find("span", class_="a-size-small", attrs={"aria-hidden": "true"}).get_text(strip=True)
        except:
            reviews = " "

        try:
            price = book.find("span", class_="_cDEzb_p13n-sc-price_3mJ9Z").get_text(strip=True)
        except:
            price = " "

        data.append([book_name, author, rating, reviews, price])

    # --- Step 5: Save results to Excel ---
    if data:
        df = pd.DataFrame(data, columns=["Book Name", "Author", "Rating", "Reviews", "Price"])
        df.to_excel(output_file, index=False)
        print(f"✅ Data has been successfully saved to {output_file}")
    else:
        print("⚠️ No book data found in the HTML file.")


if __name__ == "__main__":
    scrape_amazon_html()
