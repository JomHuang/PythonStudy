"""
读取数据,
注意:方法的大小写问题
"""

import shelve;

db = shelve.open('class-shelve');
for key in db:
    print (key, '=>', db[key]);

# 调用对象中的方法
bob = db['bob'];
print (bob.lastname());
