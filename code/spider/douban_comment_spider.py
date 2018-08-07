'''
爬取豆瓣《騎士団長殺し》的短评
参考：https://zhuanlan.zhihu.com/p/20423182
'''


import requests
import codecs    # 中文编码处理
from bs4 import BeautifulSoup

# 换别的书，只用改动这里的地址
URL = 'https://book.douban.com/subject/26952467/comments/'

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    comments_soup = soup.find('div', attrs={'id': 'comments'})
    comments = []
    for comment_item in comments_soup.find_all('p', attrs={'class': 'comment-content'}):
        comment = comment_item.getText()
        comments.append(comment)

    next_page_li = soup.find('div', {'class': 'paginator-wrapper'}).find_all('li', attrs={'class': 'p'})[2:3]
    for item in next_page_li:
        if item.find('a'):
            return comments, URL + item.find('a')['href'] 
    return comments, None



def main():
    url = URL

    with codecs.open('comments', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            comments, url = parse_html(html)
            fp.write(u'{comments}\n'.format(comments='\n'.join(comments)))

if __name__ == '__main__':
    main()