# variable scope = where a variable is visible and accessible
# scope resolution = (LEBG) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

print("------------------------")


def func1():
    x = 1

    def func2():
        print(x)

    func2()


func1()

print("------------------------")

def func1():
    print(x)

def func2():
    print(x)

x =3

func1()
func2()

print("------------------------")

from math import e

def func1():
    print(e)

e = 3

func1()