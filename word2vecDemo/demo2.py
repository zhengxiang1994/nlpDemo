# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging

# 引入日志文件
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 引入数据集
raw_sentences = ["the quick brown fox jumps over the lazy dogs", "yoyoyo you go home now to sleep"]

# 切分单词
sentences = [s.split() for s in raw_sentences]
print(sentences)

# 构建模型
model = word2vec.Word2Vec(sentences, min_count=1)

# 进行相关性比较
print("similarity is:", model.similarity("dogs", "you"))