from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
secret = "XXXXXXXXXXXXXXXX"
wait_time = 0.5

#用途ディレクトリ(train,validation,test,...)
dirword = sys.argv[1]
#label名
label = sys.argv[2]
#検索ワード
keyword = sys.argv[2]
#複数ワード検索
#keyword = sys.argv[2] + " " + sys.argv[3]

savedir = "./" + dirword + "/" + label

# FlickrAPIの実行
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = keyword,
    per_page = 500,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license',
    page = 1
)
# 画像データの格納
photos = result['photos']
#
print("\n -- Image Scraping Start -- \n\n")
print("         Running            ")
for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)

print("\n\n -- Image Scraping Finish -- \n")
