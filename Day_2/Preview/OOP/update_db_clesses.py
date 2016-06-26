"""
更新数据
"""

import shelve;

db=shelve.open('class-shelve');

bob=db['bob'];
#给BOB加薪0.25
bob.giveRaise(0.25);
db['bob']=bob;

sue=db['sue'];
#给sue加薪0.20
sue.giveRaise(0.20);
db['sue']=sue;

