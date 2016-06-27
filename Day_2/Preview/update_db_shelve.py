# 更新shelve中记录

from initdata import tom;
import shelve;
from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();
dbfilename = people_file_path.READ_PEOPLE_SHELVE_PATH();

db = shelve.open(dbfilename);
sue = db['sue'];

sue['pay'] += 1000;
db['sue'] = sue;

db['tom'] = tom;

db.close();
