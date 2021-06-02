from requests import get
from bs4 import BeautifulSoup
import math
from urllib.parse import parse_qs

BASE_URL = 'https://news.naver.com/main' #Basic Settings
browser = {'User-Agent':'Mozilla/5.0'}
domain = {'속보': '001',
        '정치': '100',
        '경제': '101',
        '사회': '102',
        '생활/문화' : '103',
        '세계': '104',
        'IT/과학': '105'
        }

def get_page(page_url):
    page = get(page_url, headers=browser)
    soup = BeautifulSoup(page.content, 'html.parser')
    return page, soup

def get_domain_headlines(domain_name):
    try:
        if domain_name == ('생활' or '문화'):
            domain_number = domain.get('생활/문화')
            headlines_url = f"{BASE_URL}/list.nhn?mode=LSD&mid=sec&sid1={domain_number}"
            return headlines_url
        elif domain_name == ('IT' or '과학'):
            domain_number == domain.get('IT/과학')
            headlines_url = f"{BASE_URL}/list.nhn?mode=LSD&mid=sec&sid1={domain_number}"
            return headlines_url
        else:
            domain_number = domain.get(domain_name)
            headlines_url = f"{BASE_URL}/list.nhn?mode=LSD&mid=sec&sid1={domain_number}"
            return headlines_url
    except:
        return "유효한 분야가 아닙니다"

def get_one_article(url):
    page, soup = get_page(url)
    article_url = url
    return 


def get_articles(headlines_url, num):
    if headlines_url.split('&')[2].lstrip('sid1=') == '001':
        page, soup = get_page(headlines_url)
        clusters = soup.find_all(class_='nclicks(fls.list)')
        publishers = soup.find_all(class_="writing")

        press_id_col = []
        press_name_col = []
        article_url_col = []
        names = []
        for i in range(0 ,num, 2):
            k = clusters[i].attrs['href'].split('&')

            press_id = k[3].lstrip('oid=')
            press_name = publishers[i].text.strip()
            article_url = k[4].lstrip('aid=')

            press_id_col.append(press_id)
            press_name_col.append(press_name)
            article_url_col.append(article_url)


        return press_id_col, press_name_col, article_url_col

    else:
        page, soup = get_page(headlines_url)
        clusters = soup.find_all(class_='cluster_text')
        publishers = soup.find_all(class_="cluster_text_press")

        press_id_col = []
        press_name_col = []
        article_url_col = []
        names = []
        for i in range(0, num, 2):
            k = clusters[i].find('a').attrs['href'].split('&')

            press_id = k[3].lstrip('oid=')
            press_name = publishers[i].text.strip()
            article_url = k[4].lstrip('aid=')

            press_id_col.append(press_id)
            press_name_col.append(press_name)
            article_url_col.append(article_url)

        return press_id_col, press_name_col, article_url_col

def get_press_number(url):
    press_num = parse_qs(url)
    return press_num['oid']

def get_article_text(headlines_url, press_number, article_number):
    domain_num = headlines_url.split('&')[2]
    article_url = f"https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&{domain_num}&oid={press_number}&aid={article_number}"
    soup, page = get_page(article_url)
    article_title = page.find(id='articleTitle').text.strip()
    article_txt = page.find(id='articleBodyContents').text.strip()
    return article_title, article_txt

def get_one_article_text(url):
    article_url = url
    soup, page = get_page(url)
    article_title = soup.find(id='articleTitle').text.strip()
    article_txt = soup.find(id='articleBodyContents').text.strip()
    return article_title, article_txt

