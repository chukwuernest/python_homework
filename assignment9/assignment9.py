import time
import json
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# TASK 3
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
time.sleep(5)  

results = []


items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")

for item in items:
    try:
       
        title_elem = item.find_element(By.CSS_SELECTOR, "h2.cp-title a")
        title = title_elem.text.strip()

      
        author_elems = item.find_elements(By.CSS_SELECTOR, "span.cp-author a")
        authors = "; ".join([a.text.strip() for a in author_elems]) if author_elems else "N/A"

       
        format_year_elem = item.find_element(By.CSS_SELECTOR, "div.cp-format span")
        format_year = format_year_elem.text.strip()

      
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })
    except Exception as e:
        print(f"Error processing item: {e}")


driver.quit()


df = pd.DataFrame(results)
print(df)

# TASK4
df.to_csv("assignment9/get_books.csv", index=False)


with open("assignment9/get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
    
# TASK6

driver.get("https://owasp.org/www-project-top-ten/")
time.sleep(5)  

vulnerabilities = []


items = driver.find_elements(By.XPATH, "//div[@id='top-10']//li/a")
for item in items:
    title = item.text.strip()
    href = item.get_attribute("href")
    vulnerabilities.append({"Title": title, "Link": href})


driver.quit()


for vuln in vulnerabilities:
    print(f"{vuln['Title']}: {vuln['Link']}")


with open("assignment9/owasp_top_10.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Title", "Link"])
    writer.writeheader()
    writer.writerows(vulnerabilities)   

