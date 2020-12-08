
def print_hello():
    print('hello helen')

#print('Hello,Python!')
print('Hello,Python!')

'''
学习python的基本语法
这是第四节的内容

'''

"""
另外一种注释方法

"""
#行与缩进

print('hello helen')
print('hello helen')

if True:
    print("True")
else:
    print('False')

if False:
  print ("Answer")
  print ("True")
else:
  print ("Answer")
  print ("False")

a=1
b=2
c=3

total=a+b+c
print("total=",total)

str='Runabc'
print(str[1:-2])
print(str[2:])
print(str[1:5:2])
print(str*2)
print(str+str)
print('hello\nrunoob')
print(r'hello\nrunoob')

#input('\n\n按下enter键后退出.')

import sys; y = 'runoob'; sys.stdout.write(y + '\n')



expression=2

if expression==1:
    print('expression=1')
elif expression==2:
    print('expression=2')
else :
    print('expression', expression)


x='a'
y='b'
#换行输出
print(x)
print(y)

print('-----------')
#不换行输出
print(x,end="")
print(y,end="")
print()

import sys
print('==============Python import mode===============')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)

from sys import argv,path #导入特定的成员

print('==============Python import mode===============')
print('path:',path)

counter=100
miles=1000.0
name='runoob'
print("\n")
print(counter)
print(miles)
print(name)

print()
"""

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典

"""
a,b,c,d=20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))

print()
"""
a=111
isinstance(a,int)
True

含义是什么?isinstance的意思是“判断类型”
"""
var1=1
var2=10
#del var1
print('var1+var2=',var1+var2)

print()

"""
5+4
4.3-2
3*7
2/4   #除法,得到一个浮点数
2//4  #得到一个整数
17%3  #取余
2**5  #取幂
"""

word='Python'
print(word[0],word[5])
print(word[-1],word[-6])

print()

list=['abcd',786,2.23,'runoob',70.2]
tinylist=[123,'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list+tinylist)

a=[1,2,3,4,5,6]
a[0]=9
a[2:5]=[13,14,15]
print(a)
print()

letters=['r','u','n','o','c','b']
print(letters[1:5:3])
print()

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)
if 'Runoob' in sites:
    print('Runoob在集合中')
else:
    print('Runoob不再集合中')
print( )

a=set('abracadabra')
b=set('alacazam')
print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

print()

dict={}
dict["one"]="1-菜鸟教程"
dict[2]="2-菜鸟工具"

tinydict={'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(dict["one"])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

Abc= {x: x**2 for x in (2, 4, 6)}
print(Abc)


print()
a=21
b=10
c=0

c=a+b
print("1-c的值:",c)

c=a-b
print("2-c的值:",c)

c=a*b
print("3-c的值:",c)

c=a/b
print("4-c的值:",c)

c=a%b
print("5-c的值:",c)

a=2
b=3
c=a**b
print("6-c的值:",c)

a=10
b=5
c=a//b
print ("7 - c 的值为：", c)

print()

a = -60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

print(bin(60))
print(bin(-60))
print(format(60, '#b'))
print(format(-60, 'b'))

c = a & b  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2  # 15 = 0000 1111
print("6 - c 的值为：", c)

print()

a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

print()

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

print()

a,b=0,1  #斐波纳契数列
while b<10:
    print(b)
    a,b=b,a+b #先计算右边,同时赋值给左边

print()
a,b,n,m=0,1,0,0
while b<10:
    print(b)
    n=b
    m=a+b
    a=n
    b=m


print()

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

print("\n")

a=1

"""
while a<7:
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
    a +=1

age = input("请输入你家狗狗的年龄: ")
age = int(age)
print("")
if age<=0:
    print("你在逗我吧!")
elif age==1:
    print("相当于 14 岁的人。")
elif age==2:
    print("相当于 22 岁的人。")
elif age>2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

"""
"""
number=7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

"""
"""
num=int(input("请输入一个数字:"))
if num%2==0:
    if num%3==0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2,但不能整除3")
else:
    if num%3==0:
        print("你输入的数字可以整除3,但不能整除2")
    else:
        print("你输入的数字不能整除2和3")
"""
a=1
while a<20:
    print(a,end=',')
    a+=3

n = 100

print("\n")

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum)) #%d表明打印整数

print(" ")

count = 0
while count < 10:
   print (count, " 小于 10")
   count = count + 1
else:
   print (count, " 大于或等于 10")

print(" ")

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x,end=',')

print("\n ")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

print(" ")

for i in range(-5,5,2):
    print(i,end=',')

print("\n")

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i],end=',')
print("\n")

sites=['Google','Wiki','Weibo','Runoob','Baidu']
for site in sites:
    if len(site)!=4:
        continue  #跳过循环块中的剩余语句,继续下一轮循环.
    print(f"Hello,{site}")  #特别注意列表元素的打印方法.
    if site=="Runoob":
        break  #跳出for和While的循环体.
print("Done!")

n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n,end=',')
print("循环结束.")

for letter in 'Runoob':
    if letter=='b':
        break
    print('当前字母为:',letter, end=',')

print("\n")

var=10
while var>0:
    var=var-1
    if var>5:
        continue #跳过下面的打印循环体
    print("当前变量值:",var,end=',')
print("Good bye!")

print("\n")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')