from initdata import bob,tom,sue;
import pickle;
"""
每条记录使用一个pikele文件
"""
for(key,record) in [('bob',bob),('tom',tom),('sue',sue)]:
    recfile=open(key+'.pkl','wb');
    pickle.dump(record,recfile);
    recfile.close();

