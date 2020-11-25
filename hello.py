
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
