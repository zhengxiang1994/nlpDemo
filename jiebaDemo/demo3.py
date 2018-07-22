# -*- coding: utf-8 -*-

import jieba
import jieba.analyse

line = "近年来云计算技术变得越来越成熟。你不仅漂亮而且温柔"
print("/".join(jieba.cut(line)))


jieba.load_userdict("dict.txt")
jieba.analyse.set_stop_words("stopwords.txt")

print("/".join(jieba.analyse.extract_tags(line)))   # topK参数未使用

