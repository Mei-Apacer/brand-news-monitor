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

    # 中文＋英文 Google News RSS
    rss_urls = [
        f'https://news.google.com/rss/search?q={keyword}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant',
        f'https://news.google.com/rss/search?q={keyword}&hl=en-US&gl=US&ceid=US:en'
    ]

    for rss_url in rss_urls:

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

# 去除重複新聞
news_df = news_df.drop_duplicates(subset=['Title'])

# 依日期輸出檔名
filename = f'brand_news_{datetime.now().strftime("%Y%m%d")}.csv'

# 輸出 CSV
news_df.to_csv(filename, index=False, encoding='utf-8-sig')

print(f'新聞報表已輸出：{filename}')
