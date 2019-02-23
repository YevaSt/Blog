# print("hello,world")

#{a=input("enter your name")
# print("hello,",a)
# b=input("enter your last name")
# print("hello,",a,b)
# print(1 in [1,2,3])
# print(6 in [1,2,3])
# if 6 in [1,2,3]:
#     print ("yes")
# elif 3 in [1,2,3]:
#     print ("ok")
# else :
#     print ("no")
# a=int(input("enter yout age"))
# if a>=18:
#     print ("you are mature")
# elif a<0 :
#     print("error")
# else:
#     print ("sorry, you are too young")
# for item in (1,3,5,7,9):
#     print(item+1)
# a=0
# while a<10:
#     a=a+1
#     print (a)
def sum(a,b):
    return a+b
a=sum(2,9)
print(a)
class Cat:
    fluffy=15
    age=2
    name="kotik"
    def murr(self):
        print ("murr")
    def __init__(self,name="kotik"):
        self.name=name
a= Cat("kotik2")
print(a.name)
a.murr()