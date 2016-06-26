import pickle;

"""
打开文件
"""
dbfile=open('people-pickle','rb');
db=pickle.load(dbfile);
dbfile.close();

db['sue']['pay']*=1.20;
db['tom']['name']='Tom Josn'

"""保存文件"""
dbfile=open('people-pickle','wb');
pickle.dump(db,dbfile);
dbfile.close();