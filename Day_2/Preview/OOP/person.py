"""
开始OOP学习
1.结构
2.封装
3.定制
定义一个类
"""


class Person:
    # 相当与构造函数
    def __init__(self, name, age, pay=0, job=None):
        self.name = name;
        self.age = age;
        self.pay = pay;
        self.job = job;

    # 取lastname
    def lastname(self):
        return self.name.split()[-1];

    # 加薪
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent);

    # 格式化输出 理解不了
    def __str__(self):
        return '<%s => %s : %s : %s>' % (self.__class__.__name__, self.name, self.job, self.pay);


if __name__ == "__main__":
    bob = person('Bob Smith', 42, 40000, 'software');
    sue = person('Sue Jones', 45, 50000, 'hardware');
    print ('bob name:', bob.name, '\n sue pay:', sue
           .pay);

    print (bob.name.split()[-1]);
    sue.pay += 200;
    print (sue.pay);

    print (bob.lastname());
    sue.giveRaise(0.2);
    print (sue.pay);
