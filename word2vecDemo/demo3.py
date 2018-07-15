# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# trian phase
'''
# 加载语料
sentences = word2vec.Text8Corpus("text8")
model = word2vec.Word2Vec(sentences, size=200)
# 保存模型
model.save("text8.model")
'''

# model 读取
model1 = word2vec.Word2Vec.load("text8.model")

# 推断相似词汇 topn: 输出相似度最高的n个
print(model1.most_similar(positive=["woman", "king"], negative=["man"], topn=3))
print(model1.doesnt_match("breakfast cereal dinner lunch".split()))
print(model1.similarity("woman", "man"))
print(model1.most_similar(["man"]))

# 获得某个单词的向量表示
print(model1["computer"])



