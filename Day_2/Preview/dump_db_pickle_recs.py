"""
使用全局glob模块获取整个数据库文件
"""

import pickle,glob

#获取全部的数据文件
for filename in glob.glob('*.pkl'):
    recfile=open(filename,'rb');
    record=pickle.load(recfile);
    print (filename,'=>',record);

#获取单个文件数据
suefile=open('sue.pkl','rb');
suecord=pickle.load(suefile);
print (suecord['name']);