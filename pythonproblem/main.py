# import random
#
#
series = [0,1,1,0]

#
# for i in range(5):
#     series.append(random.randint(0,5))
#     for j in range(i+1):
#         if
# print(series)


#
# for i in range(5):
#     count =0
#     for j in range(i):
#         list = [i]
#         if list[-1]!=0 and j in series:
#             count+=1
#         list.append(count)
#         series.append(count)
#         print(list,end="")
#     print()


for i in range(5):
    count=0
    for j in range(i+1):
        list=[]
        if j in series:
            count+=1
        list.append(count)
        print(list, end="")
    print()


