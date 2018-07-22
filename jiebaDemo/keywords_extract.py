# -*- coding: utf-8 -*-

from jieba import analyse

text = "线程是程序执行时的最小单位，它是进程的一个执行流，\
        是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，\
        线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。\
        线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。\
        同样多线程也可以实现并发操作，每个请求分配一个线程来处理。"

# based on tfidf
keywords1 = analyse.extract_tags(text)
print("keywords by tfidf:", "/".join(keywords1), sep="\n")

# based on textrank
# 提取关键词的textrank是基于窗口的，i.e.,
# 如果两个顶点相应的语义单元共同出现在一个窗口中（窗口大小从2-10不等, 那么就连接这两个顶点
keywords2 = analyse.textrank(text)
print("keywords by textrank:", "/".join(keywords2), sep="\n")


