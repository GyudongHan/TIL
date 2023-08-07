import requests
from bs4 import BeautifulSoup
import pandas as pd 
from fake_useragent import UserAgent

def getSoup(com_code):
    url = 'https://finance.naver.com/item/main.naver?code=' + com_code
    ua = UserAgent()
    
    # 기존 user-agent와 원리는 같음. 다만, 이런 라이브러리가 존재한다 정도로만 확인
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def getPrice(com_code):
    soup = getSoup(com_code)
    no_today = soup.select_one("p.no_today") # print(no_today)로도 html 소스 일부를 확인할 수 있음
    price = no_today.select_one("span.blind").get_text()
    return price

def main():
    com_codes = ["352820", "041510", "035900", "122870"]
    com_names = ["하이브", "에스엠", "JYP Ent.", "와이지엔터테인먼트"]

    prices = []
    for code in com_codes:
        price = getPrice(code)
        prices.append(price)
    
    df = pd.DataFrame({"종목코드":com_codes, "상장회사":com_names, "주가":prices})
    print(df)
    # 실제 주가를 크롤링 한다면 아래처럼 해당 주가의 날짜(시기)를 입력해도 좋겠다.
    # df['날짜'] = "오늘날짜"
    # print(df)
        
if __name__ == "__main__":
    main()