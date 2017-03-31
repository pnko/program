# split
items = "zero one two three".split()
print(items)

example ='python, jquery, javascript'
lan1, lan2,lan3 = example.split(",")
print(lan1, lan2, lan3)

url_ex ='www.naver.com'
url_ex.split(".")
print(url_ex.split("."))


# join
example =['python', 'jquery', 'javascript']
result = ''.join(example)
print(result)
print(','.join(example))

# List Comprehension
result =[i for i in range(10) if i % 2 ==0]
print("List Comprehension:", result)

word_1 = "Hello"
word_2 = "world"
result = [i+j for i in word_1 for j in word_2 ]
print(result)

# cross join
case_1 = ["A","B","C"]
case_1 = ["D","E","A"]
result = [i+j for i in case_1 for j in case_1 if not(i==j)]
result.sort()
print(result)


words = "zero one two three".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)

#Enumerate
for i , v in enumerate( ["A","B","C"]):
    print(i, v)

mylist = ["a", "b",  "c", "d"]
print(list(enumerate(mylist)))

items = {i:j for i, j in enumerate("zero one two three".split())}
print(items)

# Zip : index 끼리 묶는 것
alist = ["a1","a2","a3"]
blist = ["b1","b2","b3"]
for a, b in zip(alist,blist):
    print(a,b)

suma=[sum(x) for x in zip((1,2,3),(10,20,30))]
print(suma)
