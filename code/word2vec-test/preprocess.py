import jieba

novel = open('./三体全集.txt', 'r')
content = novel.read()
novel_segmented = open('./三体全集_segmented.txt', 'w')

cutword = jieba.cut(content, cut_all=False)
seg = ' '.join(cutword).replace(',','').replace('。','').replace('“','').replace('”','').replace('：','').replace('…','').replace('！','').replace('？','').replace('~','').replace('（','').replace('）','').replace('、','').replace('；','')
print(seg, file=novel_segmented)

novel.close()
novel_segmented.close()