"""
person的替代实现,包含数据、行为和重载(未用于对象持久化操作)
"""


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name;
        self.age = age;
        self.pay = pay;
        self.job = job;

    def lastName(self):
        return self.name.split()[-1];

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent);

    def __str__(self):
        return '<%s => %s:%s:%s>' % (self.__class__.__name__, self.name, self.job, self.pay);


# 重载一个类
class Manager:
    """
    自定义函数
    重写加薪方法
    """

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'Manager');

    def giveRaise(self, percent, bouns=0.1):
        Person.giveRaise(self, (percent + bouns));


# main
if __name__ == "__main__":
    bob = Person('Bob Smith', 42);
    sue = Person('Sue Jones', 47, 40000, 'dev');
    tom = Manager('Tom Done', 50, 50000);
    print(sue, sue.pay, sue.lastName());
    for obj in (bob, sue, tom):
        obj.giveRaise(0.1);
        print(obj);
