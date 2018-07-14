from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

vectorizer  = CountVectorizer()
corpus = [
    "This is the first document.", 
    "This is the second second document.", 
    "And the third one,", 
    "Is this the first document?",
]
X = vectorizer.fit_transform(corpus)
# output the numbers of words in each document
print(X.toarray())
# output the words extracted from the document (as the dictionary)
print(vectorizer.get_feature_names())

# idf(w,d) = log[(n_d+1) / (1+df(w,d))]
# then L2 normalization
transformer = TfidfTransformer()
tfidfs = transformer.fit_transform(X.toarray())
# output the tfidfs of words in each document
print(tfidfs.toarray())
