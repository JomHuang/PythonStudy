import pickle;
from Day_2.DataFiles.DataFilePath import DataFilePath

people_file_path = DataFilePath();
dbfilename = people_file_path.READ_PEOPLE_PICKLE_PATH();

dbfile=open(dbfilename,'rb');
db=pickle.load(dbfile);
for key in db:
    print (key,'=>',db[key]);
print (db['tom']['name']);