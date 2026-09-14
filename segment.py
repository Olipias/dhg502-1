import jieba

sentence = "我来到北京清华大学参观人工智能实验室"
seg_list = jieba.lcut(sentence)
print(" / ".join(seg_list))
