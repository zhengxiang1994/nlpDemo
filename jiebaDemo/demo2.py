# -*- coding: utf-8 -*-
import jieba


# construct stopwords list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# segment the sentences
def seg_sentence(sentence, filepath):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(filepath)
    outstr = []
    for word in sentence_seged:
        if word not in stopwords:
            if word != "\t":
                outstr.append(word)
    return "/".join(outstr)


if __name__ == "__main__":
    line = "你不仅漂亮而且温柔"
    print("no using stopwords:", "/".join(jieba.cut(line)), sep="\n")
    print("using stopwords:", seg_sentence(line, "stopwords.txt"), sep="\n")


