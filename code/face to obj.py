# 面对对象:类与实例化 类变量以及方法 私有变量和私有方法 封装 继承 多态
class bman:
    def __init__(self, name, points, rebounds, assists, steals, blocks):  # 传入参数,并定义
        self.name = name
        self.Points = points  # 得分
        self.Rebounds = rebounds  # 篮板
        self.Assists = assists  # 助攻
        self.Steals = steals  # 抢断
        self.Blocks = blocks  # 盖帽

    def getall(self):
        print(
            f"{self.name}的得分是{self.Points},篮板是{self.Rebounds},助攻是{self.Assists},抢断是{self.Steals},盖帽是{self.Blocks}")


# 类似结构体的用法

bman1 = bman("wangyi", 70, 19, 21, 5, 4)
bman1.getall()


# 类继承的例题 临时员工和正式员工,临时日结,正式月薪
class member:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Realmember(member):
    def __init__(self, id, name, month_salary):
        super().__init__(id, name)
        self.month_salary = month_salary
        self.isReal = True

    def speakstatus(self):
        print(f"{self.name}是正式员工")

    def wholesalary(self):
        print(f"{self.name}的月薪是{self.month_salary}")


class Tempmember(member):
    def __init__(self, id, name, day_salary):
        super().__init__(id, name)
        self.day_salary = day_salary
        self.isReal = False

    def speakstatus(self):
        print(f"{self.name}不是正式员工")

    def wholesalary(self):
        whole = self.day_salary * 30
        print(f"{self.name}的月薪是{whole}")


a = Realmember(1, "卢本伟",5000)
b = Tempmember(2, "马飞飞",80)
a.speakstatus()
b.speakstatus()
a.wholesalary()
b.wholesalary()
