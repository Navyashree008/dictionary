a = [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}] 
b = []
i = 0
while i < len(a):
#     key = input ("the key:")
#     if a[i][key] not in b:
#         b.append(a[i][key])
#     i+=1
# print(b)
    for x in a[i].values():
        if x not in b:
            b.append(x)
    i+=1
print(b)