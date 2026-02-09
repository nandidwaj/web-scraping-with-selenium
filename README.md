# Selenium Web Scraping Portfolio

This repository contains my hands-on learning and practical implementation of **web scraping using Selenium in Python**. The goal of this project was to understand how modern websites work, how data is loaded dynamically, and how to extract structured data reliably from real-world websites.

---

## 🎯 Objectives

Through this project, I learned to:

* Distinguish **Static vs Dynamic websites**
* Work with **HTML, DOM, CSS Selectors, and XPath**
* Use **Explicit Waits** instead of hard sleeps
* Handle **popups, overlays, and login modals**
* Implement **Infinite Scrolling**
* Implement **Pagination**
* Extract structured data and store it in **CSV format**
* Avoid duplicate data during scraping
* Navigate websites using search instead of hardcoded URLs

---

## 🌐 Websites Scraped

| Website             | Technique Used                     | Purpose                                          |
| ------------------- | ---------------------------------- | ------------------------------------------------ |
| **Myntra**          | Infinite Scroll + XPath + Selenium | Product data extraction from multiple categories |


---

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **CSV module**
* Chrome WebDriver

---

## 📁 What’s inside this repo

```
selenium-web-scraping-portfolio/
│
├── Task1.py                     # Basic Selenium practice & pagination
├── Task2.py                     # Keyword-based multi-category scraper
├── output/
│   │
│   ├──Task1.csv                   # Final scraped dataset
│   └── Task2.csv                  # Final scraped dataset
└── README.md                    # Project documentation
```

---

## 🚀 How to run the code

### Step 1 — Install dependencies

```bash
pip install selenium
```

### Step 2 — Download ChromeDriver

Make sure your Chrome version matches your ChromeDriver version.

### Step 3 — Run any script

```bash
python Task2.py
```

---

## 📊 Sample Data Extracted

Each product record includes:

* Product ID
* Brand Name
* Product Name
* Image URL
* Selling Price
* MRP Price
* Discount Percentage
* Rating
* Review Count
* Listing Type (Ad/Organic)
* Source Page (keyword used)

---

## 🧠 What I learned

This project helped me understand:

* How JavaScript renders data dynamically
* Why Selenium is needed for modern websites
* How to design robust selectors
* How to structure scraped data using lists and dictionaries
* How to export data into tabular formats like CSV

---
