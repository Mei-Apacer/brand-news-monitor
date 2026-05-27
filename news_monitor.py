import feedparser
import pandas as pd
from datetime import datetime

# 品牌關鍵字
keywords = [
    'Apacer',
    '宇瞻',
    'Innodisk',
    '宜鼎'
]

results = []

for keyword in keywords:
    rss_url = f'https://news.google.com/rss/search?q={keyword}'

    feed = feedparser.parse(rss_url)

    for entry in feed.entries[:10]:
        results.append({
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

# 輸出檔案
filename = f'brand_news_{datetime.now().strftime("%Y%m%d")}.csv'

news_df.to_csv(filename, index=False, encoding='utf-8-sig')

print(f'新聞報表已輸出：{filename}')
