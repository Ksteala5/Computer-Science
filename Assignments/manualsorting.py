import random
a = random.randint(1,101)
b = random.randint(1,101)
c = random.randint(1,101)
d = random.randint(1,101)
e = random.randint(1,101)
numbers = [a,b,c,d,e]
def bubble_sort(n):
    for i in range(0, len(n)-1):
        if n[i]>n[i+1]:
            n[i], n[i+1] = n[i+1], n[i]
    print(n)

bubble_sort(numbers)