# interactive queries
"""
路径问题没有解决
"""
import shelve;
from Day_2.DataFiles.DataFilePath import DataFilePath;

people_file_path = DataFilePath();

fieldnames = {'name', 'age', 'job', 'pay'};
maxfield = max(len(f) for f in fieldnames);

db = shelve.open(people_file_path.CLASS_SHELVE_PATH);

while True:
    key = input('\nkey?=>');
    if not key: break;
    try:
        record = db[key];
    except:
        print('No such key "%s"!' % key);
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field));
