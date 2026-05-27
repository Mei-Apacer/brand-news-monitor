import feedparser
import pandas as pd
from datetime import datetime

results = []

# 中文新聞來源（台灣）
tw_searches = [
    '宇瞻',
    'Apacer 宇瞻',
    '宜鼎',
    'Innodisk 宜鼎'
]

# 英文新聞來源（全球）
en_searches = [
    'Apacer',
    'Innodisk'
]

# 台灣中文新聞
for keyword in tw_searches:

    rss_url = f'https://news.google.com/rss/search?q={keyword}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

    feed = feedparser.parse(rss_url)

    for entry in feed.entries[:30]:

        results.append({
            'Language': 'Chinese',
            'Keyword': keyword,
            'Title': entry.title,
            'Source': entry.source.title if 'source' in entry else 'Unknown',
            'Published': entry.published if 'published' in entry else '',
            'Link': entry.link
        })

# 國際英文新聞
for keyword in en_searches:

    rss_url = f'https://news.google.com/rss/search?q={keyword}&hl=en-US&gl=US&ceid=US:en'

    feed = feedparser.parse(rss_url)

    for entry in feed.entries[:20]:

        results.append({
            'Language': 'English',
            'Keyword': keyword,
            'Title': entry.title,
            'Source': entry.source.title if 'source' in entry else 'Unknown',
            'Published': entry.published if 'published' in entry else '',
            'Link': entry.link
        })

# 建立 DataFrame
news_df = pd.DataFrame(results)

# 去除重複
news_df = news_df.drop_duplicates(subset=['Title'])

# 排序
news_df = news_df.sort_values(by='Published', ascending=False)

# 檔名
filename = f'brand_news_{datetime.now().strftime("%Y%m%d")}.csv'

# 匯出
news_df.to_csv(filename, index=False, encoding='utf-8-sig')

print(f'新聞報表已輸出：{filename}')
