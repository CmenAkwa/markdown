def shan_xing(du, r):
    squal = du / 360 * 3.14 * r ** 2
    return squal


a = "asd"
print("hello world " + a)
for i in range(0, 11):
    print(i)
p = 3j
# 虚数complex类型
print(p ** 2)
list_genshin = ["刻晴", "甘雨", "胡桃"]
print(list_genshin)
list_genshin.append("asd")
# 添加
print(list_genshin)
price = [100, 200, 300]
print(price)
max_price = max(price)
print(max_price)
min_price = min(price)
print(min_price)
sorted_price = sorted(price)
contact = {"小明": 15919460000, "小花": 15919460001, ("老王", 3): 100000000,
           ("老王", 4): 15919410002}  # 大括号是字典，前 键 后 值,键只能是常量
print(contact["小明"])  # 类数组写法,可用元组,元组是不可变常量,
print(contact[("老王", 3)])  # 圆括号元组
contact["卢本伟"] = 156194  # 添加值,存在则修改值
if "卢本伟" in contact:  # 判断是否存在，返回布尔值
    print(contact["卢本伟"])
else:
    print("不存在")
del (contact["卢本伟"])  # 删除字典
if "卢本伟" in contact:  # 判断是否存在，返回布尔值
    print(contact["卢本伟"])
else:
    print("不存在")
total = 0
for i in range(1, 101):  # i=1;i<101,i++
    total += i
print(total)
user_input = 0
the_sum = 0
cnt = -1
"""while user_input != 'p':
    user_input = int(user_input)
    the_sum += user_input
    cnt += 1
    user_input = input("以p结尾,请输入数字:")
print("总数为" + str(the_sum))
print(cnt)
if cnt == 0:
    print("0")
else:
    print(the_sum / cnt)"""
for name in contact:  # 键迭代
    phone = contact[name]
    print("{0}的电话号码是:{1}".format(name, phone))  # 格式化输出

print(shan_xing(180, 2))
print(list_genshin[0:3])  # 切片左闭右开，i=0;i<3;i++
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list_1)):
    print(list_1[i])
list_2 = []
for i in range(len(list_1)):
    if list_1[i] % 2 == 0:
        list_2.append(list_1[i] ** 2)
print(list_2)
list_3 = [i * i for i in range(1, 10) if (i % 2 == 1)]
print(list_3)
asdd = 100
print("asdd是", asdd)


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("除数不能为0")  # 抛出错误信息
    else:
        return x / y


try:
    print(division(1, 0))
except BaseException as msg:  # 接收至msg
    print(msg)


def doubler(n):
    return (n * 2)


numbers = [1, 2, 3, 4, 5]
result = map(doubler, numbers)  # map函数,对列表进行操作
print(list(result))


def isdouble(n):
    return n % 2 == 0


numbers = filter(isdouble, numbers)  # number是1 2 3 4 5
#filter筛选函数,前是筛选函数，后是被筛选对象,返回
print(list(numbers))#转换为列表输出
