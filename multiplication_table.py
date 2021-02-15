# in correct order:-
# num = int(input("enter the number"))
# tables = {}
# i = 1
# while i <= num:
#     a = []
#     for j in range(1,11):
#         a.append(i*j)
#     tables[i]= a
#     i+=1
# print(tables)

# in reverse order:-
num = int(input("enter the number"))
tables = {}
i = num
while i >= 1:
    a = []
    for j in range(1,11):
        a.append(i*j)
    tables[i] = a
    i-=1
print(tables)