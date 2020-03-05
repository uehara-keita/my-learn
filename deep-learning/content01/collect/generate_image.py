from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = []
num_classes = len(classes)
IMAGE_SIZE = 224

X = []
Y = []

print("\n --  Image Data Generate Start -- \n\n")
print("         Running            ")
for index, classlabel in enumerate(classes):
    # クラスごとのディレクトリを指定
    photo_dir = './' + classlabel
    # jpg形式の画像ファイルを取得
    files = glob.glob(photo_dir + '/*.jpg')
    for i, file in enumerate(files):
        # 画像ファイルを開く
        image = Image.open(file)
        # カラースケール指定
        image = image.convert('RGB')
        # 画像のサイズ変換
        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
        # 画像データから配列
        data = np.asarray(image)
        
        X.append(data)
        Y.append(index)
print("\n\n --  Image Data Generate Finish -- ")

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,Y)
xy = (X_train, X_test, y_train, y_test)
np.save('./image_files.npy', xy)