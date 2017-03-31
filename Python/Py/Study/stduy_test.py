"""print("Enter your name")
sb=input()
print("Hi", sb)
"""
"""
temper = float(input("온도를 입력하세요:"))
print(temper)
print(type(temper))
"""

"""
print("본 프로그램은")
print("변환하고")
user_input=input()
fah=((9/5) * float(user_input))+32
print("섭씨:", user_input)
print("화씨:", fah)
"""
for i in range(10):
    if i == 5:
        break
    print(i)


print("EOP")


kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [23, 39, 40, 60, 70]

def additon(x,y): 
    return x+y

def multiplication(x, y):
    return x*y

def divided_by_2(x):
    return x/2

def main():
    print(additon(10, 5))
    print(multiplication(10, 5))

def spam(eggs):
    eggs.append(1)
    eggs=[2, 3]
    print(eggs)

ham=[0]
spam(ham)
print(ham)
if __name__ == '__main__':
    main()
