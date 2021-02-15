# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# high = 0
# high2 = 0
# high3 = 0
# for x in my_dict:
#     # print(x)
#     # print(my_dict[x])
#     if x > high:
#         high3 = high2
#         high2 = high
#         high = x
# print(x)


# d ={ 
#   "fantasy": "harrypotter", 
#   "romance": "me before you", 
#   "fiction": "divergent"
#   } 
    
# # places the tuples in a list. 
# print(d.items()) 
  
# # returns iterators and never builds a list fully. 
# print(d.iteritems()) 

num =int(input("enter number"))
a = num // 10
if a == 7:
    print("yes")
else:
    print("no")