from initdata import bob, tom, sue;
import pickle;
from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();

"""
每条记录使用一个pikele文件
"""
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(people_file_path.READ_PEOPLE_PICKLE_RECS_PATH(key + '.pkl'), 'wb');
    pickle.dump(record, recfile);
    recfile.close();
