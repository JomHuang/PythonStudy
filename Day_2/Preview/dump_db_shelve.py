#读取shelve中的数据

import shelve;

db=shelve.open('people-shelve');
for key in db:
    print (key,'=>',db[key]);

print (db['tom']['pay']);

db.close();