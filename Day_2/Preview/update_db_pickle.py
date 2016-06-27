import pickle;

from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();
dbfilename = people_file_path.READ_PEOPLE_PICKLE_PATH();

"""
打开文件
"""
dbfile=open(dbfilename,'rb');
db=pickle.load(dbfile);
dbfile.close();

db['sue']['pay']*=1.20;
db['tom']['name']='Tom Josn'

"""保存文件"""
dbfile=open(dbfilename,'wb');
pickle.dump(db,dbfile);
dbfile.close();