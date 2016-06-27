"""
读取数据,
注意:方法的大小写问题
"""

import shelve;
from Day_2.DataFiles.DataFilePath import DataFilePath;

people_file_path = DataFilePath();


db = shelve.open(people_file_path.CLASS_SHELVE_PATH);
for key in db:
    print (key, '=>', db[key]);

# 调用对象中的方法
bob = db['bob'];
print (bob.lastname());
