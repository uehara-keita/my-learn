import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model, load_model
from PIL import Image
import sys, cv2

#モデルのクラス名
classes = ['duck', 'pigeon', 'swan', 'hawk', 'sparrow']
num_classes = len(classes)

# 画像データの変換
IMAGE_SIZE = 224

image = Image.open(sys.argv[1])
image = image.convert('RGB')
show_img = image
image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
data = np.asarray(image)
X = []
X.append(data)
X = np.array(X)

# モデルのロード
model = load_model('./model-1.h5')

# 推定結果
print("*"*30,"\n")
print("-- Forecast Result --\n")

result = model.predict([X])[0]
predicted = result.argmax()
percentage = int(result[predicted] * 100)

image.show()

print(classes[predicted], percentage,"%\n")
print("*"*30)