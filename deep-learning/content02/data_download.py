import os
import urllib.request
import zipfile
import tarfile

print('-'*20 + 'Download start' + '-'*20)
url = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
save_path = "./data/aclImdb_v1.tar.gz"
if not os.path.exists(save_path):
    urllib.request.urlretrieve(url, save_path)
print('-'*20 + 'Download finish' + '-'*20)



# './data/aclImdb_v1.tar.gz'の解凍　1分ほどかかります
print('-'*20 + 'file open start' + '-'*20)
# tarファイルを読み込み
tar = tarfile.open('./data/aclImdb_v1.tar.gz')
tar.extractall('./data/')  # 解凍
tar.close()  # ファイルをクローズ
print('-'*20 + '\file open finish' + '-'*20)
# フォルダ「data」内にフォルダ「aclImdb」というものができます。
