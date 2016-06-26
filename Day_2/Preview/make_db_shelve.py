"""
  键值对形式的数据库存储
"""

from initdata import bob,tom,sue;
import shelve;

db=shelve.open('people-shelve');
db['bob']=bob;
db['tom']=tom;
db['sue']=sue;
db.close();