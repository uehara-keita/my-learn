import tarfile
import glob
import os
import io
import string
import sys

train = sys.argv[0]
test = sys.argv[1]

# train
if (train == True):
    print('-'*20 + 'train tsv start' + '-'*20)
    f = open('./data/IMDb_train.tsv', 'w')

    path = './data/aclImdb/train/pos/'
    for fname in glob.glob(os.path.join(path, '*.txt')):
        with io.open(fname, 'r', encoding="utf-8") as ff:
            text = ff.readline()

            # タブがあれば消しておきます
            text = text.replace('\t', " ")

            text = text+'\t'+'1'+'\t'+'\n'
            f.write(text)

    path = './data/aclImdb/train/neg/'
    for fname in glob.glob(os.path.join(path, '*.txt')):
        with io.open(fname, 'r', encoding="utf-8") as ff:
            text = ff.readline()

            # タブがあれば消しておきます
            text = text.replace('\t', " ")

            text = text+'\t'+'0'+'\t'+'\n'
            f.write(text)
    f.close()
    print('-'*20 + 'train tsv finish' + '-'*20)

else:
    print("passed train")

#test
if (test == True):
    print('-'*20 + 'test tsv start' + '-'*20)
    f = open('./data/IMDb_test.tsv', 'w')

    path = './data/aclImdb/test/pos/'
    for fname in glob.glob(os.path.join(path, '*.txt')):
        with io.open(fname, 'r', encoding="utf-8") as ff:
            text = ff.readline()

            # タブがあれば消しておきます
            text = text.replace('\t', " ")

            text = text+'\t'+'1'+'\t'+'\n'
            f.write(text)


    path = './data/aclImdb/test/neg/'

    for fname in glob.glob(os.path.join(path, '*.txt')):
        with io.open(fname, 'r', encoding="utf-8") as ff:
            text = ff.readline()

            # タブがあれば消しておきます
            text = text.replace('\t', " ")

            text = text+'\t'+'0'+'\t'+'\n'
            f.write(text)

    f.close()
    print('-'*20 + 'train tsv finish' + '-'*20)

else:
    print("passed test")