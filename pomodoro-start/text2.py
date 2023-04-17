import numpy

# my_input = input("")
# my_list = [int(x) for x in my_input if x.isdigit()]
# my_array = numpy.array(my_list)
# my_array.shape = (3,3)
# print(my_array)

# my_list = []
# dimensions = input("")
# my_dimensions = [int(x) for x in dimensions if x.isdigit()]
# i = 0
# while i < my_dimensions[0]:
#     rows = input("")
#     my_rows = [int(x) for x in rows if x.isdigit()]
#     my_list.append(my_rows)
#     i += 1
# print(my_list)
# my_array = numpy.array(my_list)
# my_transpose =my_array.transpose()
# my_flatten = my_array.flatten()
# print(my_transpose)
# print(my_flatten)


# import numpy
#
# N,M,P = map(int,input().split())
# arr_1 = []
# arr_2 = []
# for i in range(N):
#     arr_1.append(list(map(int,input().split())))
#
# for j in range(M):
#     arr_2.append(list(map(int,input().split())))
#
# arr_1 = numpy.array(arr_1)
# arr_2 = numpy.array(arr_2)
# print(numpy.concatenate((arr_1,arr_2),axis=0))


# def split_and_join(line):
#     # write your code here
#     list = line.split(" ")
#     join_list = "-".join(list)
#     return join_list
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)


# i,j = input().split()
# print(i)
# print(j)

a = input().split()
print(a)