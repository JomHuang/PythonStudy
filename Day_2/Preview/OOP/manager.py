from person import Person

"""
继承
1.自定义构造函数
"""


class Manager(Person):
    # 自定义构造函数
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'Manager')

    # 重写加薪方法
    def giveRaise(self, percent, Bonus=0.1):
        # self.pay*=(1.0+percent+Bonus);
        Person.giveRaise(self, percent + Bonus);  # 换一种写法


if __name__ == "__main__":
    tom = Manager(name='Tom Done', age=20, pay=50000);
    Jom = Manager('Jom Don', 20, 30000);
    print (tom.lastname());
    tom.giveRaise(0.2);
    print (tom.pay);
