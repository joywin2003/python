N = int(input())
list = []
response = input("")
response = response.split(" ")
while N > 0:
    if response[0] == "insert":
        list.insert(int(response[2]), int(response[1]))
        N -= 1
    elif response[0] == "print":
        print(list)
        N -= 1
    elif response[0] == "remove":
        list.remove(int(response[1]))
        N -= 1
    elif response[0] == "append":
        list.append(int(response[1]))
        N -= 1
    elif response[0] == "sort":
        list.sort()
        N -= 1
    elif response[0] == "pop":
        list.pop()
        N -= 1
    elif response[0] == "reverse":
        list.reverse()
        N -= 1


