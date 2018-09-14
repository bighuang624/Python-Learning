from gensim.models import word2vec

#import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 训练 word2vec 模型，生成词向量
s = word2vec.LineSentence('./三体全集_segmented.txt')

# size: 词向量维度
# window: 窗口大小
# min_count: 词语的频数少于该值时忽略
# workers: 并行数
model = word2vec.Word2Vec(s, size=20, window=5, min_count=5, workers=4)

model.save('wordvec_model.pkl')
model = word2vec.Word2Vec.load('wordvec_model.pkl')

# 打印词向量
print(model['叶文洁'])

# 打印相似度最高的词
y = model.most_similar('叶文洁', topn=5)  # 5 个最相似的
print('和【叶文洁】最相似的词有：\n')
for item in y:
    print(item[0], item[1])