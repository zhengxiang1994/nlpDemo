# -*- coding: utf-8 -*-
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

if __name__ == "__main__":
    sentences = [
        "我来到北京清华大学",
        "他来到了网易杭研大厦", 
        "小明硕士毕业于中国科学院", 
        "我爱北京天安门"
     ]
    corpus = []
    for sentence in sentences:
        corpus.append(" ".join(jieba.cut(sentence)))
    # print the corpus after cutting
    print("new corpus:", corpus, sep="\n")

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    # output the terms extracted from copus
    word = vectorizer.get_feature_names()
    print("terms extracted from corpus:", word, sep="\n")
    # output the numbers of terms in each document
    print("terms in each document:", X.toarray(), sep="\n")
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    # output the weights of each term in each document
    weight = tfidf.toarray()
    print("tf-idf:", np.array(weight), sep="\n")

    for i in range(len(weight)):
        print(u"-------这里输出第", i, u"类文本的词语tf-idf权重-------", "# 该类文本对应的是:", sentences[i])
        for j in range(len(word)):
            print(word[j], weight[i][j])




