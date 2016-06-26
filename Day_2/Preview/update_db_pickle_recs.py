"""
更新其中一个数据文件
"""

import pickle;

dbfile=open('sue.pkl','rb');
db=pickle.load(dbfile);
dbfile.close();

db['pay']*=1.3

dbfile=open('sue.pkl','wb');
pickle.dump(db,dbfile);
dbfile.close();