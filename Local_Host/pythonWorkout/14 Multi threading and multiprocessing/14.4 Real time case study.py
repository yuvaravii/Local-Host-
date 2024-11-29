import threading
from bs4 import BeautifulSoup
import requests

urls = ["https://en.wikipedia.org/wiki/MS_Dhoni", "https://en.wikipedia.org/wiki/Virat_Kohli", "https://en.wikipedia.org/wiki/Sachin_Tendulkar"]

def fetch_content(url):
    print(f"Fetching content for URL: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Extracted characters count : {len(soup.text)}  --> from url : {url}")

threads = []

for url in urls:
    print(f"Starting thread for URL: {url}")
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
