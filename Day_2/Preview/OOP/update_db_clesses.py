"""
更新数据
"""

import shelve;
from Day_2.DataFiles.DataFilePath import DataFilePath;

people_file_path = DataFilePath();

db=shelve.open(people_file_path.CLASS_SHELVE_PATH);

bob=db['bob'];
#给BOB加薪0.25
bob.giveRaise(0.25);
db['bob']=bob;

sue=db['sue'];
#给sue加薪0.20
sue.giveRaise(0.20);
db['sue']=sue;

