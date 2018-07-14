# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as pseg

words = jieba.cut("他来到了网易杭研大厦")
print("/".join(words))

# 加入自定义词典
jieba.load_userdict("dict.txt")
words = jieba.cut("他来到了网易杭研大厦")
print("/".join(words))

words = jieba.cut("近年来云计算技术变得越来越成熟")
print("/".join(words))

# 允许程序在运行的时候，动态的修改词典
words = jieba.cut("我们中出了一个叛徒", HMM=False)
print("/".join(words))

words = jieba.cut("我们中出了一个叛徒", HMM=False)
jieba.suggest_freq("中出", True)
print("/".join(words))

# 词性标注
words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print("{0}, {1}".format(word, flag))

# 三种模式的分词
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("full mode:" + "/".join(seg_list))   # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("accurate mode:" + "/".join(seg_list))   # 精确模式

seg_list = jieba.cut("我来到北京清华大学")
print("default mode:" + "/".join(seg_list))   # 默认是精确模式

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("/".join(seg_list))   # 搜索引擎模式




