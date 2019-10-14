



class Oya():
    def oya_func(self):
        print("I am OYA")

class Kodomo(Oya):
    def kodomo_func(self):
        print("I am Kodomo")

k = Kodomo()

k.oya_func()
k.kodomo_func()



'''
import sys
for i in sys.argv:
    print(i)

# ターミナルで「python3 test001.py hoge fuga foo」と入力すると
test001.py
hoge
fuga
foo
'''



'''
class Example():

    def __init__(self, a,b,c):
        self.num1 = a
        self.num2 = b
        self.num3 = c

    def print_tot(self):
        tot = self.num1+self.num2+self.num3
        print(tot)

myinstance = Example(1,2,3)
myinstance.print_tot()
'''

'''
class MyClass():
    #__init__ コンストラクタ、self インスタンス自身を指す
    def __init__(self, message):
        self.value = message

#インスタンスを代入する変数名 = クラス名(引数) と呼び出し
myinstance = MyClass("Hello!")
print(myinstance.value)
'''





'''
class Hoge:
    def __init__(self, hoge, fuga):
        self.hoge = hoge
        self.fuga = fuga
    def getHoge(self):
        print(self.hoge)
    def getFuga(self):
        print(self.fuga)

h = Hoge("hoge", "fuga")
'''


'''
for i in range(100):
    if i % 3 == 0 and i % 5 ==0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
    else:
        print(i)
'''


'''
l = [i for i in range(100)]
print(l)

#100以下の３の倍数
l = [i for i in range(100) if i % 3 == 0]
print(l)
#100以下の15の倍数
l = [i for i in range(100) if i % 15 == 0]
print(l)
'''



'''
s = set()

s.add(1)
s.add(2)
s.add(1)
s.add('foo')

for i in s:
    print(i)
'''


'''
obj = {'hoge': 'hoge', 'fuga': 1, 'foo': True}
for k in obj:
    print(k)
#辞書オブジェクトをそのままfor文で回すとキーkeyが取得できる。
for k in obj:
    print(k + ": " + str(obj[k]))
'''



'''
mylist = ['hoge', 'fuga', 100, 'foo', True]
for i in mylist:
    print(i)
'''


'''
mylist = [11, 1, 3, 5, 3, 6, 7, 8, 9, 23, 23, 5]
myset = set(mylist)
print(myset)
'''

'''
A = {1,2,3,7,11}
B = {3,4,5,6,7,11}

C = A ^ B
print(C)
'''

'''
A = {1,2,3,7,11}
B = {3,4,5,6,7,11}

C = A - B
print(C)
'''

'''
A = {1,2,3,7,11}
B = {3,4,5,6,7,11}

C = A & B
print(C)
'''

'''
A = {1,2,3}
B = {3,4,5,6,7,11}

C = A | B
print(C)
'''

'''
myset = set([1,2,3])
myset.remove(3)
print(myset)
'''


'''
myset = set([1,2,3])
myset.add(4)
print(myset)
'''


'''
obj = {'hoge': 'hoge', 'fuga': 1}
print(obj['hoge'])

obj['foo'] = 2 #データを追加
print(obj['foo'])

del obj[hoge] #データを削除
print(obj['hoge'])
'''


'''
d1 = {"apple": "りんご","B": 2,"C": 3}
print(d1["apple"])
'''


'''
def sum(a, b, c):
    print(a + b + c)

sum(a=1, b=2, c=3)
'''

'''
def main():
    print("hoge")

main()
'''

#str = "Hello" + " " + "World!"
#print(str)
