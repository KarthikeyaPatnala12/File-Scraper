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
all_links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        all_links.append(href)

# find all links that contain "/wp-content/"
wp_content_links = []
for link in all_links:
    if "/wp-content/" in link:
        wp_content_links.append(link)

# save the wp-content links to a CSV file
filename = url.replace("http://", "").replace("https://", "").replace("/", "") + "_wp_content_links.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["WP-Content Links"])
    for link in wp_content_links:
        writer.writerow([link])

# print out the File links
print("File links found on the website:")
for link in all_links:
    print(link)


print(f"File links saved to {os.path.abspath(filename)}")
