# import requests
# from bs4 import BeautifulSoup
# import csv
#
# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
#
# r = requests.get(url)
#
# soup = BeautifulSoup(r.text, "html.parser")
#
# # boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# # print(len(boxes))
# names = soup.find_all("a", class_ = "title")
#
# for i in  names:
#     print(i.text)
#
# prices = soup.find_all("h4", class_ = "float-end price card-title pull-right")
#
# for i in  prices:
#     print(i.text)
#
# df.to_csv("scraping.csv")


import requests
from bs4 import BeautifulSoup
import csv

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

names = soup.find_all("a", class_="title")
prices = soup.find_all("h4", class_="float-end card-title")

# Create a list to store the data
data = []

for name, price in zip(names, prices):
    product_name = name.text.strip()
    product_price = price.text.strip()
    data.append([product_name, product_price])

# Write the data to a CSV file
with open("scraping.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write headers
    csvwriter.writerow(["Product Name", "Product Price"])

    # Write data rows
    csvwriter.writerows(data)

print("Data has been scraped and saved to scraping.csv")
