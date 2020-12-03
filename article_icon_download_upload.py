import os
import requests
import uuid

from django.core.files import File

from article.models import Articlefrom article.models import Article


articles = Article.objects.all()

for article in articles:
    if article.icon:
        res = requests.get(article.icon.url)
        print(res)
        if res.status_code == 403:
            url = article.icon.url.replace('stc.1144378.com', 'static.0a5.com')
            res = requests.get(url)
            if res.status_code == 200:
                image_file_name = os.path.basename(article.icon.url)
                img_data = res.content
                with open(f'{image_file_name}', 'wb') as handler:
                    handler.write(img_data)
                article.icon.save(image_file_name, File(open(image_file_name, 'rb')))
                os.remove(image_file_name)


for article in articles:
    if article.icon:
        staging_file_size = requests.head(article.icon.url).headers['content-length']
        production_file_size = requests.head(article.icon.url.replace('stc.1144378.com', 'static.0a5.com')).headers['content-length']
        if not staging_file_size == production_file_size:
            print(article)
            url = article.icon.url.replace('stc.1144378.com', 'static.0a5.com')
            res = requests.get(url)
            if res.status_code == 200:
                uuid_prefix = str(uuid.uuid4())[:8]
                image_file_name = f'{uuid_prefix}-{os.path.basename(article.icon.url)}'
                img_data = res.content
                with open(f'{image_file_name}', 'wb') as handler:
                    handler.write(img_data)
                article.icon.save(image_file_name, File(open(image_file_name, 'rb')))
                os.remove(image_file_name)

article = Article.objects.get(id=137)
