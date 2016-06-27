"""
  键值对形式的数据库存储
"""

from initdata import bob, tom, sue;
import shelve;

from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();
dbfilename = people_file_path.READ_PEOPLE_SHELVE_PATH();

db = shelve.open(dbfilename);
db['bob'] = bob;
db['tom'] = tom;
db['sue'] = sue;
db.close();
