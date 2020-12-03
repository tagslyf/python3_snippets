import requests

from django.core.files import File

from article.models import Article


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

