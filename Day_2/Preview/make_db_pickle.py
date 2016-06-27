from initdata import db;
import pickle;
from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();
dbfilename = people_file_path.READ_PEOPLE_PICKLE_PATH();

dbfile = open(dbfilename, 'wb');  # 使用3.x的二进制模式文件
pickle.dump(db, dbfile);  # 字节数据,并不是字符串
dbfile.close();
