from gensim import corpora, models, similarities
import logging
from collections import defaultdict
import numpy as np

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# docs
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
# 1. split and remove discontinuation words
stoplist = set("for a of the and to in".split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
print(texts)
print("-*-" * 30)

# 2. calculate the frequency of words
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# choose the words whose frequency bigger than 1
texts = [[token for token in text if frequency[token]>1] for text in texts]
print(texts)
print("-*-" * 30)

# 3. construct the dictionary
dictionary = corpora.Dictionary(texts)
print(dictionary.token2id)
print("-*-" * 30)

# 4. a new doc
new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())   # 采用稀疏表示的方式返回结果
print(new_vec)
print("-*-" * 30)

# 5. construct corpus
corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus)
print("-*-" * 30)

# 6. init the model
tfidf = models.TfidfModel(corpus)
# test
test_doc_bow = [(0, 1), (1, 1)]
print(tfidf[test_doc_bow])
print("-*-" * 30)
# change entire corpus to the representation of tfidf
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)
print("-*-" * 30)

# 7. construct the index
index = similarities.MatrixSimilarity(corpus_tfidf)

# 8. calculate the similarity
new_vec_tfidf = tfidf[new_vec]
print(new_vec_tfidf)
print("-*-" * 30)

# calculate the similarity between new doc and each doc in texts
sims = index[new_vec_tfidf]
print(sims)
print("-*-" * 30)

sim_arr = []
for doc_tfidf in corpus_tfidf:
    sim_arr.append(index[doc_tfidf])
print(np.array(sim_arr))





