import requests, csv
from bs4 import BeautifulSoup

url = requests.get('https://coreyms.com').text
soup = BeautifulSoup(url, 'lxml')
articles = soup.find_all('article')

csv_file = open('website_content.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['TITLE', 'SUMMARY', 'VIDEO LINK'])

for article in articles:
    post_title = article.h2.a.text
    post_summary = article.find('div', class_='entry-content').p.text

    try:
        raw_link = article.find('iframe', class_='youtube-player')['src']
        vid_id = raw_link.split('?')[0]
        vid_id = vid_id.split('/')[4]
        yt_link = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = 'Video does not exist'

    print(post_title.upper())
    print(post_summary)
    print(yt_link)
    print()
    print()

    csv_writer.writerow([post_title, post_summary, yt_link])

csv_writer.close