#Write a Python program that utilizes the requests and BeautifulSoup libraries to scrape the main page of Wikipedia (https://www.wikipedia.org/). The program should first retrieve the HTML content of the webpage. If successful (status code 200), it should then parse the HTML and find all heading elements (h1 to h6). Finally, the program should extract and print the text content of these headings after removing any leading or trailing whitespace.
import requests
from bs4 import BeautifulSoup

# Wikipedia URL to scrape
url = 'https://en.wikipedia.org/wiki/Main_Page'

# Send a GET request to the Wikipedia page
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the HTML elements containing the titles (class may vary, inspect the webpage to find the correct class)
    headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Print the titles
    for headline in headlines:
        print(headline.text.strip())
else:
    print(f"Failed to retrieve the Wikipedia page. Status code: {response.status_code}")

