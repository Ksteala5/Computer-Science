import random
numbers = [random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101),]
print(numbers)
def bubble_sort(n):
    steps = 0
    for j in range (0, len(n)-1):
        for i in range(0, len(n)-1):
            if n[i]>n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
                steps += 1
    print(n)
    print(str(steps)+" steps.")

bubble_sort(numbers)