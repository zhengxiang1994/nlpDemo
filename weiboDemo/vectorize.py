# -*- coding: utf-8 -*-
from weiboDemo.xml_extract import get_corpus
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import scale


texts, tags = get_corpus("datasets/evsam02.xml")

print(texts)

vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(texts))
weight = tfidf.toarray()
features = np.array(weight)
print(weight.shape)

sel = SelectKBest(chi2, k=100)
features_new = sel.fit_transform(features, tags)
print(features_new)
features_new = scale(features_new)

train_x, test_x, train_y, test_y = train_test_split(features_new, tags, test_size=0.2, random_state=0)
print("true labels:", test_y)
svc = SVC()
svc.fit(train_x, train_y)
pred_y = svc.predict(test_x)
print("predicted labels:", pred_y)
print(accuracy_score(test_y, pred_y))





