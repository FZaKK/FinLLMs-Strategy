import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_stock_news():
    url = "http://guba.eastmoney.com/list,usnvda,1,f.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到新闻条目的部分
        news_items = soup.find_all('tr', class_='listitem')

        '''
        提取新闻标题、链接、作者、发布时间和阅读总数等
        其中阅读总数可以表征重要性与关注度
        '''
        news_data = []
        for item in news_items:
            link = "http://guba.eastmoney.com" + item.find('div', class_='title').find('a')['href']
            title = item.find('div', class_='title').find('a').text.strip()
            author = item.find('div', class_='author').find('a').text.strip()
            # print(author)
            pub_time = item.find('div', class_='update').text.strip()
            total_read = item.find('div', class_='read').text.strip()

            news_data.append({'title': title, 'link': link, 'author': author,
                              'pub_time': pub_time, 'total_read': total_read})

        return news_data
    else:
        print("Failed to fetch news.")
        return None


'''
df = pd.DataFrame(columns=['标题', '链接', '作者', '发布时间', '阅读总数'])
stock_news = get_stock_news()
# 遍历 stock_news 列表，将数据添加到 DataFrame 中
for news in stock_news:
    df = pd.concat([df, pd.DataFrame([[news['title'],
                                       news['link'],
                                       news['author'],
                                       news['pub_time'],
                                       news['total_read']]],
                                     columns=['标题', '链接', '作者', '发布时间', '阅读总数'])],
                   ignore_index=True)

df.to_excel('stock_news.xlsx', index=False)
'''

# 获取并打印最新的股票新闻
stock_news = get_stock_news()
if stock_news:
    for news in stock_news:
        print("标题:", news['title'])
        print("链接:", news['link'])
        print("作者:", news['author'])
        print("发布时间:", news['pub_time'])
        print("阅读总数:", news['total_read'])
        print()
