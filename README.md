# KQC7016 Lab 1 Web Scraping

## Group Members
- Nie Jing 25069019
- Dai Fenfang 25069603

## Lab Description
This repository contains the files for KQC7016 Lab 1: Web Scraping.

The purpose of this lab is to study the original lab1.py code, understand the function of each part of the code, and modify the code to perform web scraping on another website.

## Website Used
The modified web scraping program uses:

https://quotes.toscrape.com/

This website was selected because it is designed for web scraping practice and contains structured quote and author information.

## Files Included
- `original_lab1.py` - Original Python file studied and executed for Lab 1.
- `Lab1_WebScraping.py` - Modified Python source code for scraping quotes and authors.
- `quotes_with_authors.csv` - Output CSV file containing the extracted quotes and authors.
- `Lab_Report_1_Web_Scraping.docx` - Lab 1 report.
- `README.md` - Repository description and file explanation.

## Libraries Used
- requests
- BeautifulSoup
- pandas

## Output
The Python program extracts:
- Quote
- Author

The extracted data is saved as:

`quotes_with_authors.csv`

## Ethical Consideration
Before scraping the website, the robots.txt file should be checked:

https://quotes.toscrape.com/robots.txt

This is important to consider the ethical issue of web scraping.

## How to Run
Run the original Python file using:

```bash
python original_lab1.py
