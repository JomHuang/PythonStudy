#读取shelve中的数据

import shelve;
from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();
dbfilename = people_file_path.READ_PEOPLE_SHELVE_PATH();

db=shelve.open(dbfilename);
for key in db:
    print (key,'=>',db[key]);

print (db['tom']['pay']);

db.close();