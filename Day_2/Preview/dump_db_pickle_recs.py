"""
使用全局glob模块获取整个数据库文件
"""

import pickle, glob;
from Day_2.DataFiles.DataFilePath import DataFilePath;

people_file_path = DataFilePath();

# 获取全部的数据文件
for filename in glob.glob(people_file_path.READ_PEOPLE_PICKLE_RECS_PATH('*.pkl')):
    recfile = open(filename, 'rb');
    record = pickle.load(recfile);
    print(filename, '=>', record);

# 获取单个文件数据
suefile = open(people_file_path.READ_PEOPLE_PICKLE_RECS_PATH('sue.pkl'), 'rb');
suecord = pickle.load(suefile);
print(suecord['name']);
