import requests
from bs4 import BeautifulSoup
import pandas as pd

def createDF(result_list):
    result_df = pd.DataFrame({"title" : result_list})
    return result_df

def crawler(soup):
    tbody = soup.find("tbody")
    result = []
    for p in tbody.find_all("p", class_ = "title"):
        result.append(p.get_text().replace('\n',""))
    return result

def main():
    custom_header = {
        'referer': 'https://www.google.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    url = "https://music.bugs.co.kr/chart"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    result = crawler(soup)
    df = createDF(result)
    print(df)

if __name__ == "__main__":
    main()