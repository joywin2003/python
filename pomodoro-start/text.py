a = input()
l_case = [char for char in a if char.islower()]
l_case.sort()
u_case = [char for char in a if char.isupper()]
u_case.sort()
num_odd = [num for num in a if num.isdigit() and int(num)%2 != 0]
num_odd.sort()
num_even = [num for num in a if num.isdigit() and int(num)%2 == 0]
num_even.sort()

final_list = l_case + u_case + num_odd + num_even
final_word = "".join(final_list)
print(final_word)

