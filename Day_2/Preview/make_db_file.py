"""
用自定义格式将内存数据库对象保存到文件中;
假定数据中不使用'endrec','enddb','=>';
假定数据库是字典:警告:使用evel可能存在危险,它会将字符串当作代码执行;
也可以用evel()一次创建一条字典记录
对于print(key,file=dbfie),也可以使用dbfile.write(key+'\n');
"""

dbfilename = "people-file";
ENDDB = 'enddb.';
ENDREC = 'endrc.';
RECSEP = '=>';


def storeDbase(db, dbfilename=dbfilename):
    "将数据库文件保存为普通文件"
    dbfile = open(dbfilename, 'w');
    for key in db:
        print (key, file = dbfile);
        for (name, value) in db[key].items():
            print (name + RECSEP + repr(value), file = dbfile);
        print (ENDREC, file = dbfile);
    print (ENDDB, file = dbfile);
    dbfile.close();


def loadDbase(dbfilename=dbfilename):
    "解析数据,重新构建数据库"
    dbfile = open(dbfilename)
    import sys;
    sys.stdin = dbfile;
    db = {};
    key = input();
    while key != ENDDB:
        rec = {};
        field = input();
        while field != ENDREC:
            name, value = field.split(RECSEP);
            rec[name] = eval(value);
            field = input();
        db[key] = rec;
        key = input();
    return db


if __name__ == '__main__':
    from initdata import db;
    storeDbase(db)