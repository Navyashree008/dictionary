string = "MISSISSIPPI"
my_dict = {}
i = 0
while i < len(string):
    a = string[i]
    j = 0
    count = 0
    while j <len(string):
        if string[j] == a:
            count = count+1
        j+=1
    my_dict[string[i]] = count
    i+=1
print(my_dict)