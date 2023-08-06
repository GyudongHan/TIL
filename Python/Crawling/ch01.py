# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

# index.html을 불러와서 BeautifulSoup 객체 초기화
def main():
    soup = BeautifulSoup(open("html/index.html", encoding="UTF-8"), "html.parser")
    print(soup.find("p").get_txt())
    fake_str = soup.find('div', class_ = "fakecampus").find('p').get_text()
    print(fake_str)

if __name__ == "__main__":
    main()

print(__name__)


# #특정 문자열을 가진 p 태그 크롤링
# def main():
#     soup = BeautifulSoup(open("html/index.html", encoding="UTF-8"), "html.parser")
#     print(soup.find('p', string='여기는 크롤링 해주세요!'))

# #특정 div class를 무시하고 크롤링
# def main():
#     soup = BeautifulSoup("html/index.html", 'html.parser')
#     div_tags = soup.find_all('div')
#     for div_tag in div_tags:
#         if div_tag.get('class') == ['mulcam1']:
#             continue
#         print(div_tag.text)