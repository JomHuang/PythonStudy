"""
数据持久化
"""

import shelve;
from person import Person;
from manager import Manager;
from Day_2.DataFiles.DataFilePath import DataFilePath;

people_file_path = DataFilePath();


# 初始化数据
bob = Person('Bob Smith', 42, 30000, 'software');
sue = Person('Sue Jones', 45, 40000, 'hardware');
tom = Manager('Tom Done', 44, 50000);

# 持久化
db = shelve.open(people_file_path.CLASS_SHELVE_PATH);
db['bob']=bob;
db['sue']=sue;
db['tom']=tom;
db.close();

