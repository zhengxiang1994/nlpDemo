from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import word2vec

print("the texts is:", common_texts, sep="\n")

# path = get_tmpfile("word2vec.model")
'''
size: the dimension of vector, default value is 100
window: the number of neighbors, default value is 5
min_count: the minimum times appeared in texts, default value is 5
worker: the number of threats
'''
# model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
# model.save("word2vec.model")

model = word2vec.Word2Vec.load("word2vec.model")
model.train([["hello", "world"]], total_examples=1, epochs=1)
vector = model.wv["computer"]
print(vector)

