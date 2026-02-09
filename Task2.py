"""
Keyword URLs (Scrape all 5)
    1.	https://www.myntra.com/tshirt?rawQuery=tshirt
    2.	https://www.myntra.com/shoes?rawQuery=shoes
    3.	https://www.myntra.com/jeans?rawQuery=jeans
    4.	https://www.myntra.com/dresses?rawQuery=dresses
    5.	https://www.myntra.com/jackets?rawQuery=jackets

Elements to be Scraped

    1.	Image URL
    2.	Brand Name
    3.	Product Name
    4.	Product ID (from DOM or product URL)
    5.	Selling Price
    6.	MRP Price
    7.	Discount Percentage
    8.	Rating (if available)
    9.	Comment / Review Count (if available)
    10.	Listing Type (Advertisement / Organic)
    11.	Source Page (brand / keyword)

"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv


def scroll(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        cards = driver.find_elements(By.XPATH,"//ul[@class='results-base']//li[@class='product-base']")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        new_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        if new_height == last_height:
            break
        last_height = new_height
    



options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

items_to_search = ["tshirt","shoes","jeans","dresses","jackets"]

url = "https://www.myntra.com"

driver.get(url)
time.sleep(5)

wait =  WebDriverWait(driver,10)

products_data = []
for i in items_to_search:
    search_box = driver.find_element(By.XPATH,"//div[@class='desktop-query']//input")
    search_box.clear()
    search_box.send_keys(i)
    search_box.send_keys(Keys.ENTER)

    wait.until(EC.presence_of_all_elements_located((By.XPATH,"//ul[@class='results-base']//li[@class='product-base']")))

    """scroll(driver)"""

    products = driver.find_elements(By.XPATH,"//ul[@class='results-base']//li[@class='product-base']")
    count =0
    for product in products:
        count+=1
        product_id = product.get_attribute("id")
        brand = product.find_element(By.XPATH,".//h3").text
        product_name = product.find_element(By.XPATH,".//h4").text

        driver.execute_script("arguments[0].scrollIntoView();", product)
        time.sleep(0.5)

        img_url = product.find_element(By.XPATH,".//img").get_attribute("src")

        try:
            selling_price = product.find_element(By.XPATH,".//span[@class='product-discountedPrice']").text.split()[-1]
            discount_percent = product.find_element(By.XPATH,".//span[@class='product-discountPercentage']").text.strip().replace("(", "").replace(" OFF)", "")
        except:
            selling_price = product.find_element(By.XPATH,".//div[@class='product-price']//span").text.split()[-1]
            discount_percent = 0
        try:
            mrp_price = product.find_element(By.XPATH,".//span[@class='product-strike']").text.split()[-1]
        except:
            mrp_price=selling_price
        try:
            rating = product.find_element(By.XPATH,".//span").text
            rating_count = product.find_element(By.XPATH,".//div[@class='product-ratingsCount']").text.split("\n")[-1]
        except:
            rating=0
            rating_count=0
        try:
            listing_type = product.find_element(By.XPATH,".//div[@class='product-waterMark']").text
        except:
            listing_type = "Oragnic"
        source = "Keyword : "+i

        products_data.append({
            "Product_id":product_id,
            "Brand Name":brand,
            "Product Name":product_name,
            "Image URL": img_url,
            "Selling Price":selling_price,
            "MRP Price":mrp_price,
            "Discount Percentage":discount_percent,
            "Rating":rating,
            "Comment / Review Count":rating_count,
            "Listing Type":listing_type,
            "Source Page":source,
        })
        if count==30:
            break

with open("Task2.csv","w",newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["Product_id","Brand Name","Product Name","Image URL","Selling Price","MRP Price","Discount Percentage","Rating","Comment / Review Count","Listing Type","Source Page"])
    writer.writeheader()
    writer.writerows(products_data)
print("Saved to Task2.csv")