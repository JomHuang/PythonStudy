"""
增加控制台交互更新数据
"""
import  shelve;
from person import Person;
#文件路径
from Day_2.DataFiles.DataFilePath import DataFilePath;

people_file_path=DataFilePath();

fieldnames=('name','age','job','pay');
db=shelve.open(people_file_path.CLASS_SHELVE_PATH);

while True:
    key=input('\nkey? =>');
    if not key:break;
    if key in db:
        record=db[key];
    else:
        record=Person(name='?',age='?');
    for field in fieldnames:
        currval=getattr(record,field);
        newtext=input('\t[%s]=%s\n\t\tnew?=>' % (field,currval));
        if newtext:
            setattr(record,field,eval(newtext))
    db[key]=record;
db.close();
