# my-learn-python
 A study repository for python.
 
 ## deep-learning
 深層学習に関連したファイルをまとめてあります。
 
 ### content01
 教師用画像データ収集、モデル生成、予測するプログラム
 #### collect
 【download.py】
 filckerAPIで入力した単語で検索を行い、検索結果の１ページ目から５００枚を指定したフォルダに保存します。
 【generate_image.py】
 教師画像データ群を配列(.npyファイル形式)でまとめるプログラム。
 #### models
 【dl_models.py】
 VGG16にプーリング層+全結合層(1024)+出力層(n)を重ね、14層までを凍結させ、パラメータを学習させる。
 教師画像に指定した水増しを行い、学習させたのちモデルを.h5形式で保存する。
 使用ライブラリ:Keras
 【predict.py】
 プログラム実行時に入力したファイルを推定します。出力結果として、最も確率の高いクラスラベルと確率(%)を返します。
 
 ### content02
 「[つくりながら学ぶ Pytorchによる発展ディープラーニング](https://www.amazon.co.jp/%E3%81%A4%E3%81%8F%E3%82%8A%E3%81%AA%E3%81%8C%E3%82%89%E5%AD%A6%E3%81%B6-PyTorch%E3%81%AB%E3%82%88%E3%82%8B%E7%99%BA%E5%B1%95%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%A9%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0-%E5%B0%8F%E5%B7%9D%E9%9B%84%E5%A4%AA%E9%83%8E/dp/4839970254)」を元に進めたBERTモデル
 
 
 
 
