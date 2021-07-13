import bs4
import requests

response = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
# print(response.text)

soup = bs4.BeautifulSoup(response.text, "html.parser")
content = soup.select(".mw-headline")

print(content)
for headline in content:
    print(headline.text)