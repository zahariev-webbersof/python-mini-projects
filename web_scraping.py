from bs4 import BeautifulSoup
import requests
import csv
import json


def main():
    url = 'http://yahoo.com'
    req_data = requests.get(url)
    content = req_data.text
    soup = BeautifulSoup(content, "html.parser")

    headlines = []
    for headline in soup.find_all("h3"):
        raw_headline = headline.get_text()
        headline = raw_headline.strip()
        if len(headline) < 10:
            continue
        headlines.append(headline)

    print(json.dumps(headlines))

    with open("news_data.csv", 'w') as output_file:
        writer = csv.writer(output_file, delimiter=',')
        writer.writerow(['headline'])
        for headline in headlines:
            writer.writerow([headline])

if __name__ == '__main__':
    main()