list1 = [1,2,3,4,5]
for i in list1:
    print("Element:",i)
print(list1[0])
list1.append(9)
print(list1)

for i in range (0,1001):
    print(i)


list2=["a", "b", "1", "de"]
for i in list2:
    print(i)

for i in "втипо":
    print(i)







1
a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B (больше A): "))

c = 1
for num in range(a, b+1):
    c*= num

print("Произведение всех целых чисел от", a, "до", b, "включительно равно:", c)

2
N = int(input("Введите целое число N (N > 0): "))

sum = 0
for i in range(1, N+1):
    sum += 1/i

print("Сумма ряда 1 + 1/2 + 1/3 + ... + 1/N равна:", sum)
