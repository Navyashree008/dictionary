my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
high = 0
high2 = 0
high3 = 0
for x in my_dict:
    if my_dict[x] > high:
        high3 = high2
        high2 = high
        high = my_dict[x]
print(high)
print(high2)
print(high3)   

# my_dict ={'name':'navya','age':18,'place':'banglore'}
# for x in my_dict:
#     print(x,'---->',my_dict[x])
#     # print('---->',end=" ")
#     # print(my_dict[x])
