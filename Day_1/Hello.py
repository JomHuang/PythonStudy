"""
sqlite
"""
sqlite3_PATH = "./DataFiles/somedatabase.db";
import sqlite3;

#创建数据连接,如果文件不存在就创建一个新的
conn = sqlite3.connect(sqlite3_PATH);
#获得连接的游标,这个游标可以用来执行SQL查询
curs=conn.cursor();

#提交
conn.commit();
#关闭
conn.close();