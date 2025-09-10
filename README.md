
# Web\_Scapping\_amazon

## 📌 Project Overview

This project scrapes **Amazon book listings** from a saved HTML file (`amazon.html`) using **BeautifulSoup** and extracts details such as:

* Book Name
* Author
* Rating
* Reviews
* Price

The extracted data is then exported into an **Excel file (`amazon_books.xlsx`)** for further analysis.

---

## 🚀 Features

* Parses local `amazon.html` file using BeautifulSoup
* Extracts book details (name, author, rating, reviews, price)
* Handles missing fields gracefully (stores blank if not found)
* Stores results in a clean Excel sheet
* Works around **HTTP 503 errors** by scraping from a saved HTML file instead of making live requests

---

## 📂 Project Structure

```
Web_Scapping_amazon/
│── Amazon_Scapping.ipynb   # Jupyter Notebook with scraping logic
│── amazon.html             # Saved Amazon webpage (used for parsing)
│── amazon_books.csv        # Scraped results in CSV format
│── amazon_books.xlsx       # Scraped results in Excel format (generated)
│── scraper.py              # Python script for scraping (optional)
│── README.md               # Project documentation
```

---

## ⚙️ Requirements

Install dependencies with pip:

```bash
pip install pandas beautifulsoup4 lxml openpyxl
```

---

## 📝 Usage

### 1. Clone the repository

```bash
git clone https://github.com/nishantdorwal/Web_Scapping_amazon.git
cd Web_Scapping_amazon
```

### 2. Why use a saved HTML file?

When trying to scrape Amazon directly with `requests`, the server often responds with **HTTP Error 503 (Service Unavailable)** because Amazon blocks automated scrapers.

👉 To bypass this, the webpage was saved manually as `amazon.html`, and all parsing is done on this local file. This ensures consistent results and avoids repeated 503 errors.

### Example 503 Error Log

```python
import requests

url = "https://www.amazon.in/s?k=books"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(response.status_code)
print(response.text[:500])
```

**Output:**

```
503
<!DOCTYPE html>
<html>
<head>
<title>503 - Service Unavailable Error</title>
</head>
<body>
<h1>Service Unavailable</h1>
<p>The server is currently unable to handle the request (HTTP Error 503).</p>
</body>
</html>
```

This is why the project uses a **saved HTML file** for reliable scraping.

---

### 3. Run the scraper script

```bash
python scraper.py
```

Or open the Jupyter Notebook:

```bash
jupyter notebook Amazon_Scapping.ipynb
```

### 4. Output

* An Excel file **`amazon_books.xlsx`** will be created with the following columns:

  * **Book Name**
  * **Author**
  * **Rating**
  * **Reviews**
  * **Price**

---

## 📊 Sample Output (Excel)

| Book Name            | Author        | Rating | Reviews | Price |
| -------------------- | ------------- | ------ | ------- | ----- |
| Book Title Example 1 | Author Name 1 | 4.5 ★  | 1234    | ₹499  |
| Book Title Example 2 | Author Name 2 | 4.0 ★  | 987     | ₹299  |

---

## ⚠️ Notes & Limitations

* Uses a **saved HTML file (`amazon.html`)** to avoid Amazon’s **503 response errors**.
* If Amazon changes its webpage structure, the scraper may need updates.
* Scraping Amazon directly may violate their **Terms of Service**—this project demonstrates scraping techniques using offline data.

---

## 🔮 Future Enhancements

* Automate fetching live Amazon data using `requests` & headers
* Add support for multiple categories (e.g., Bestsellers, New Releases)
* Store data in a database (SQLite / MongoDB)
* Build a simple dashboard to visualize results

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

