"""
更新其中一个数据文件
"""

import pickle;
from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();

dbfile = open(people_file_path.READ_PEOPLE_PICKLE_RECS_PATH('sue.pkl'), 'rb');
db = pickle.load(dbfile);
dbfile.close();

db['pay'] *= 1.3

dbfile = open(people_file_path.READ_PEOPLE_PICKLE_RECS_PATH('sue.pkl'), 'wb');
pickle.dump(db, dbfile);
dbfile.close();
