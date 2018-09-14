# README

本文件夹下代码基于 Python 3.5。运行时请先进入到当前目录，并确保已经安装 jieba 和 gensim。

`python preprocess.py`会使用 jieba 将文件夹中的“三体全集.txt”进行分词处理，并存储为“三体全集_segmented.txt”。

`python demo.py`会运行一个简单的 demo 来展示 Word2vec 的效果。

由于语料规模较小，因此效果不是很好，仅供参考。