import jieba
import re
from os import path 
#得到地址
d = path.dirname('.')
#d=path.dirname(__file__)
f=open('./小时代.txt', 'r',encoding='gb18030')
#得到文本
text=f.readlines()
#得到停用词
stopkey=[line.strip() for line in open('./stopword.txt').readlines()] 
#stopkey=[line.strip().decode('utf-8') for line in open('./stopword.txt',encoding='gb18030').readlines()] 
seg_list=[]
doclist=[]
for t in text:
    t=re.sub('[0-9]','',t,count=0,flags=0)
    t=re.sub('\n','',t,count=0,flags=0)
    words=list(jieba.cut(t,HMM=False))
    l=[word for word in words if len(word)>1]
    seg=" ".join(list(set(l)-set(stopkey)))
    seg_list.append(seg)
doclist=' '.join(seg_list)
with open ('./小时代分词.txt','wt') as file2:
    file2.writelines(doclist)    
print('end')
