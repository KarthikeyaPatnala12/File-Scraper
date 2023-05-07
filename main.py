import requests
from bs4 import BeautifulSoup
import csv
import os 
import urllib.parse
import warnings

# specify the URL of the website you want to scrape
url = input("Enter the URL of the website you want to scrape: ")
file_ext = input("Enter the file extension you want to scrape (e.g., .pdf, .pptx, .py): ")

warnings.filterwarnings("ignore", message="Unverified HTTPS request")
# check if the URL has a scheme, and add one if necessary
if not urllib.parse.urlparse(url).scheme:
    url = "https://" + url

    
response = requests.get(url, verify=False)

# parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")


website_name = url.split("//")[1].split(".")[0]

# find all links on the page that point to File files
file_links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and href.endswith(file_ext):
        file_links.append(href)

# save the File links to a CSV file
file_name = f"{website_name}.csv"
with open(file_name, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["File Links"])
    for link in file_links:
        writer.writerow([link])

# print out the File links
print("File links found on the website:")
for link in file_links:
    print(link)


print(f"File links saved to {os.path.abspath(file_name)}")
