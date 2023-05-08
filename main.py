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
file_links_file_name = f"{website_name}_file_links.csv"
with open(file_links_file_name, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([f"{file_ext.upper()} Links"])
    for link in file_links:
        writer.writerow([link])

# print out the File links
print(f"{file_ext.upper()} links found on the website:")
for link in file_links:
    print(link)

print(f"{file_ext.upper()} links saved to {os.path.abspath(file_links_file_name)}")

# ask the user if they want to scrape all links
scrape_all_links = input("Do you want to scrape all links on the website? (y/n): ").lower()

if scrape_all_links == 'y':
    # find all links on the page
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)

    # save all links to a CSV file
    all_links_file_name = f"{website_name}_all_links.csv"
    with open(all_links_file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Links"])
        for link in links:
            writer.writerow([link])

    # print out all links
    print("All links found on the website:")
    for link in links:
        print(link)

    print(f"All links saved to {os.path.abspath(all_links_file_name)}")
else:
    print("All links not scraped.")
